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
    print("uai: ", parsel_selector)
    return links_list


# Requisito 3
def scrape_next_page_link(html_str):
    parsel_selector = Selector(html_str)
    next_page_link = parsel_selector.css(".next::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_noticia(html_str):
    ps = Selector(html_str)
    url = ps.css("link[rel=canonical]::attr(href)").get()
    title = ps.css(".entry-title::text").get().strip()
    timestamp = ps.css(".meta-date::text").get()
    writer = ps.css(".author a::text").get()
    comments_count = len(ps.css(".comment").getall())
    summary = ps.xpath("string(//p)").get().strip()
    tags = ps.css(".post-tags a::text").getall()
    category = ps.css(".meta-category .label::text").get()

    f_locals = locals()
    var_list = ("url", "title", "timestamp", "writer", "comments_count",
                "summary", "tags", "category")
    # https://stackoverflow.com/questions/28722869/does-python-support-object-literal-property-value-shorthand-a-la-ecmascript-6
    scrape_dict = ({var: f_locals[var] for var in var_list})

    return scrape_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
