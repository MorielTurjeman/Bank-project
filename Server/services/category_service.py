from data_accses_queries import category_data
from exeptions.value_not_found_error import ValueNotFoundError


def get_categories():
    categories = category_data.get_categories()
    return categories
