from bs4 import BeautifulSoup
import requests
from scraper import config

BASE_URL = "https://stackoverflow.com/"
result_dict = {}


def scrap(keyword=""):
    query = f"jobs?r=true&q={keyword}"
    target_url = f"{BASE_URL}{query}"
    result_dict = {
        "site": "stack_overflow", "keyword": keyword, "url": target_url, "result": []}
    response = requests.get(target_url, headers=config.HEADER)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        raw_job_list = soup.find(
            "div", {"class": "listResults"}).find_all("div", {"class": "js-result"})
        for job in raw_job_list:
            job_card = config.job_card_template.copy()
            job_card["title"] = job.find(
                "a", {"class": "s-link"})["title"]
            job_card["url"] = BASE_URL + \
                job.find("a", {"class": "s-link"})["href"]
            job_card["company_name"] = job.find(
                "h3", {"class": "fc-black-700"}).find("span").text
            result_dict["result"].append(job_card)
    return result_dict
