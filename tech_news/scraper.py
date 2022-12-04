import time

import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3)

        status_code = response.status_code
        if status_code != 200:
            raise requests.HTTPError
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_novidades(html_str):
    parsel_selector = Selector(html_str)
    links_list = parsel_selector.css(".entry-title a::attr(href)").getall()

    return links_list


# Requisito 3
def scrape_next_page_link(html_str):
    parsel_selector = Selector(html_str)
    next_page_link = parsel_selector.css(".next::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
