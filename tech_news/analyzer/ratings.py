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


def top_5_ordered(dict):
    ordered_elements = sorted(
      dict.items(), key=lambda el: el[1], reverse=True)
    result = list(map(lambda el: el[0], ordered_elements[:5]))

    return result


def count_list_elements(dict_list):
    counted_elements = {}
    values_list = list(map(lambda el: el["category"], dict_list))

    for item in values_list:
        if item in counted_elements.keys():
            counted_elements[item] += 1
        else:
            counted_elements[item] = 1

    return top_5_ordered(counted_elements)


# Requisito 11
def top_5_categories():
    top_5_categories = list(get_collection().find(
        {}, {"category": True, "_id": False})
        .sort("category", 1))

    ordered_categories_count = count_list_elements(top_5_categories)

    return ordered_categories_count
