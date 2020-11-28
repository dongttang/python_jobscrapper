from flask import Flask, render_template, request
from scraper import config, remote_ok, stack_overflow, we_work_remotely


SCRAPER_LIST = config.REGISTERED_SCRAPER
headers = config.HEADER
app = Flask("DayEleven")


@app.route("/")
def home():
    return render_template("index.html", scraper_list=SCRAPER_LIST)


@app.route("/result")
def result():
    scraped_site_list = []
    keyword = request.args.get("keyword")
    print(keyword)
    for scraper_name in SCRAPER_LIST:
        if request.args.get(scraper_name):
            function_name = f"{scraper_name}.scrap"
            print(function_name + f"({keyword})")
            scraped_site_list.append(eval(function_name + f"(\"{keyword}\")"))

    return render_template("searchResults.html", scraped_site_list=scraped_site_list)


# app.run(host="0.0.0.0")
app.run(host="127.0.0.1")
