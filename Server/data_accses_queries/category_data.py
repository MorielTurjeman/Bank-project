from data_accses_queries.db_connection import connection
from models.category import Category


def create_category(name):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            create_category = f"INSERT into category( name) values('{name}')"
            cursor.execute(create_category)
            connection.commit()
            return Category(name)
    except RuntimeError as e:
        print(e)
        raise ValueError(f'Cannot create category {name}')


# def get_category(name):
#     try:
#         with connection.cursor as cursor:
#             get_category = f"Select * from category where name='{name}'"
#             cursor.execute(get_category)
#             result = cursor.fetchall()
#             return Category(name)

#     except RuntimeError as e:
#         print(e)
#         raise ValueError(f'Cannot get category {name}')


def get_categories():
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            get_category = f"Select * from category"
            cursor.execute(get_category)
            results = cursor.fetchall()
            categories: list[Category] = []
            for result in results:
                categories.append(Category(result['name']))

            return categories
    except RuntimeError as e:
        print(e)
        raise ValueError('Cannot get categorys')


# def delete_category(name):
#     try:
#         with connection.cursor() as cursor:
#             delete_query = f"delete  from category where name='{name}'"
#             cursor.execute(delete_query)
#             connection.commit()
#     except RuntimeError as e:
#         print(e)
#         raise ValueError(f"'Cannot delete category{name}'")
