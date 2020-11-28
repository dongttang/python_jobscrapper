from bs4 import BeautifulSoup
import requests

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

REGISTERED_SCRAPER = [
    "stack_overflow",
    "remote_ok",
    "we_work_remotely",
]

job_card_template = {
    "title": str,
    "company_name": str,
    "office_location": str,
    "salary_unit": str,
    "salary_amount": int,
    "last_updated": str,
    "keyword": str,
    "url": str,
}
