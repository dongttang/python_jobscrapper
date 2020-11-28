from bs4 import BeautifulSoup
import requests
from scraper import config

BASE_URL = "https://remoteok.io/"


result_dict = {}


def scrap(keyword=""):
    query = f"remote-dev+{keyword}-jobs"
    target_url = f"{BASE_URL}{query}"
    result_dict = {
        "site": "remote_ok", "keyword": keyword, "url": target_url, "result": []}
    response = requests.get(target_url, headers=config.HEADER)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        raw_job_list = soup.find(
            "table", {"id": "jobsboard"}).find_all("tr", {"class": "job"})

        for job in raw_job_list:
            job_card = config.job_card_template.copy()
            job_card["title"] = job.find(
                "h2", {"itemprop": "title"})

            job_card["url"] = BASE_URL + \
                job.find("a", {"itemprop": "url"})["href"]

            job_card["company_name"] = job.find(
                "h3", {"itemprop": "name"})
            result_dict["result"].append(job_card)
    return result_dict
