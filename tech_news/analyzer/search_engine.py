import datetime as dt

from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query_result = search_news({"title": {"$regex": title, "$options": "i"}})
    title_and_urls = []

    for element in query_result:
        title_and_urls.append((element["title"], element["url"]))

    return title_and_urls


# Requisito 7
def search_by_date(date):
    # https://www.geeksforgeeks.org/fromisoformat-function-of-datetime-date-class-in-python/
    try:
        formatted_date = dt.datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query_result = search_news({"timestamp": formatted_date})
        title_and_urls = []

        for element in query_result:
            title_and_urls.append((element["title"], element["url"]))
        return title_and_urls

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    query_result = search_news({"tags": {"$regex": tag, "$options": "i"}})
    title_and_urls = []

    for element in query_result:
        title_and_urls.append((element["title"], element["url"]))

    return title_and_urls


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    query_result = search_news(query)
    title_and_urls = []

    for element in query_result:
        title_and_urls.append((element["title"], element["url"]))

    return title_and_urls
