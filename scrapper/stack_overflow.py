from config import *

BASE_URL = "https://stackoverflow.com/"
result_dict = {}
result_dict["stack_overflow"] = []


def scrap_so(keyword=""):
    query = f"jobs?r=true&q={keyword}"
    target_url = BASE_URL + query
    result_dict["stack_overflow"] = {
        "keyword": keyword, "url": target_url, "result": []}

    response = requests.get(target_url, headers=HEADER)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        raw_job_list = soup.find(
            "div", {"class": "listResults"}).find_all("div", {"class": "js-result"})
        for job in raw_job_list:
            job_card = job_card_template.copy()
            job_card["title"] = job.find(
                "a", {"class": "s-link"})["title"]
            job_card["url"] = BASE_URL + \
                job.find("a", {"class": "s-link"})["href"]
            job_card["company_name"] = job.find(
                "h3", {"class": "fc-black-700"}).find("span").text
            result_dict["stack_overflow"]["result"].append(job_card)

        f = open("./DUMMY_codes/sample_so.json", "w")
        f.write(str(result_dict))
        f.close()

    return raw_job_list


print(scrap_so("python"))
