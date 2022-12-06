from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    top_5_data = list(get_collection().find(
        {}, {"title": True, "url": True})
        .sort("comments_count", - 1).limit(5))
    top_5_commented = []

    for data in top_5_data:
        top_5_commented.append((data["title"], data["url"]))

    return top_5_commented


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
