from data_accses_queries.db_connection import connection
from models.user import User


def get_balance(user_id):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            get_balance = f"Select current_balance from user where id={user_id}"
            cursor.execute(get_balance)
            result = cursor.fetchall()
            return result
    except RuntimeError as e:
        print(e)
        raise ValueError('Cannot get current balance')


def update_balance(user_id, transaction_amount):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            update_balance = f"update user set current_balance=current_balance+{transaction_amount} where id={user_id}"
            cursor.execute(update_balance)
            connection.commit()
    except RuntimeError as e:
        print(e)
        raise ValueError('Cannot update balance')


def add_user(user: dict):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            new_user = f"insert into user(id, first_name, last_name, current_balance) values(null, '{user['first_name']}', '{user['last_name']}', 0)"
            cursor.execute(new_user)
            connection.commit()
            return User(cursor.lastrowid, user['first_name'], user['last_name'], 0)
    except RuntimeError as e:
        print(e)
        raise ValueError(f'Cannot create user')
