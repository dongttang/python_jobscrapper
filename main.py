import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

app = Flask("DayEleven")


@app.route("/")
def home():
    return render_template("index.html")


# app.run(host="0.0.0.0")
app.run(host="127.0.0.1")