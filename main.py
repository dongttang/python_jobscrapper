from flask import Flask, render_template, request, redirect, url_for, send_file
from scraper import config, remote_ok, stack_overflow, we_work_remotely
import os
import csv


SCRAPER_LIST = config.REGISTERED_SCRAPER
headers = config.HEADER
app = Flask("DayEleven")
db = {}


def save_to_file(keyword):
    f = open(f"{keyword}.csv", mode="w")
    f.write("title, company, link\n")
    for job in db[keyword]:
        title = job["title"].text
        company = job["company_name"].text
        url = job["url"]
        row = f"{title},{company},{url}\n"
        f.write(row)
    f.close()
    return


@app.route("/")
def home():
    return render_template("index.html", scraper_list=SCRAPER_LIST)


@app.route("/result")
def result():
    scraped_site_list = []
    job_amount = 0
    keyword = request.args.get("keyword").lower()
    if len(request.args) <= 1:
        return redirect(url_for("home"))
    else:
        for scraper_name in SCRAPER_LIST:
            if request.args.get(scraper_name):
                function_name = f"{scraper_name}.scrap"
                print(function_name + f"({keyword})")
                scraped_site_list.append(
                    eval(function_name + f"(\"{keyword}\")"))
        db[keyword] = []
        for site in scraped_site_list:
            job_amount += len(site["result"])
            db[keyword] += site["result"]
    return render_template("searchResults.html",
                           scraped_site_list=scraped_site_list, job_amount=job_amount)


@app.route("/export")
def export():
    try:
        keyword = request.args.get("keyword")
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        save_to_file(keyword)
        return send_file(f"{keyword}.csv")
    except:
        return redirect("/")


# app.run(host="0.0.0.0")
app.run(host="127.0.0.1")
