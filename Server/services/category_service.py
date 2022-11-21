from data_accses_queries import category_data
from exeptions.value_not_found_error import ValueNotFoundError


def get_categories():
    categories = category_data.get_categories()
    return categories


def is_in_categories(category: str):
    catogries = get_categories()
    if category in catogries:
        return True
    else:
        return False
