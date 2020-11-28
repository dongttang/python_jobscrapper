from bs4 import BeautifulSoup
import requests
from scraper import config

BASE_URL = "https://weworkremotely.com"
result_dict = {}


def scrap(keyword=""):
    query = f"/remote-jobs/search?term={keyword}"
    target_url = f"{BASE_URL}{query}"
    result_dict = {
        "site": "we_work_remotely", "keyword": keyword, "url": target_url, "result": []}
    response = requests.get(target_url, headers=config.HEADER)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        job_section_list = soup.find_all("section", {"class": "jobs"})

        for section in job_section_list:
            raw_job_list = section.find_all("a")

            for job in raw_job_list:
                if not job.find("span", {"class": "title"}):
                    continue
                job_card = config.job_card_template.copy()
                job_card["title"] = job.find(
                    "span", {"class": "title"})
                job_card["url"] = BASE_URL + job["href"]
                job_card["company_name"] = job.find(
                    "span", {"class": "company"})

                result_dict["result"].append(job_card)

    return result_dict
