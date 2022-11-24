from data_accses_queries.db_connection import connection
from models.transaction import Transaction
from models.transaction_sum import Transaction_Sum


# def create_transaction(user_id, vendor, amount, category_name, is_deleted):
#     try:
#         with connection.cursor() as cursor:
#             create_transaction = f"INSERT into transactions(id,user_id, vendor, amount, category_name, is_deleted) values(null,{user_id}, '{vendor}', {amount}, '{category_name}',{is_deleted} )"
#             cursor.execute(create_transaction)
#             connection.commit()
#             return Transaction(cursor.lastrowid, user_id, vendor, amount, category_name, is_deleted)
#     except RuntimeError as e:
#         print(e)
#         raise ValueError(f'Cannot create transaction')

def create_transaction(transaction: dict):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            create_transaction = f"INSERT into transactions(id,user_id, vendor, amount, category_name, is_deleted) values(null,{transaction['user_id']}, '{transaction['vendor']}', '{transaction['amount']}', '{transaction['category_name']}',{transaction['is_deleted']} )"
            cursor.execute(create_transaction)
            connection.commit()
            return Transaction(cursor.lastrowid, transaction['user_id'], transaction['vendor'], transaction['amount'], transaction['category_name'])
    except RuntimeError as e:
        print(e)
        raise ValueError(f'Cannot create transaction')


def get_transactions(user_id):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            query = f"select * from transactions where is_deleted=false and user_id={user_id}"
            cursor.execute(query)
            results = cursor.fetchall()
            transaction: list[Transaction] = []
            for result in results:
                transaction.append(Transaction(
                    result['id'], result['user_id'], result['vendor'], result['amount'], result['category_name'], result['is_deleted']))
            return transaction
    except RuntimeError as e:
        print(e)
        raise ValueError('Cannot get transactions')


def delete_transaction(transaction_id, user_id):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            delete_transaction = f"update transactions set is_deleted=1 where id={transaction_id} and user_id={user_id}"
            cursor.execute(delete_transaction)
            connection.commit()
            # return {'message': 'transaction deleted'}
    except RuntimeError as e:
        print(e)
        raise ValueError(f'Cannot delete transaction id={transaction_id}')


def get_transactions_by_category(category_name, user_id):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            query = f"Select * from transactions where category_name ='{category_name}' and is_deleted='false' and user_id={user_id}"
            cursor.execute(query)
            results = cursor.fetchall()
            transaction: list[Transaction] = []
            for result in results:
                transaction.append(Transaction(
                    result['id'], result['user_id'], result['vendor'], result['amount'], result['category_name'], result['is_deleted']))
            return transaction
    except RuntimeError as e:
        print(e)
        raise ValueError(
            f'Cannot get {category_name} transactions')


def sum_transactions_by_category(user_id):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            sum_query = f"select SUM(amount) as amount, category_name from transactions where is_deleted='false' and user_id={user_id} group by category_name"
            cursor.execute(sum_query)
            results = cursor.fetchall()
            transaction_breakdown: list[Transaction_Sum] = []
            for result in results:
                transaction_breakdown.append(Transaction_Sum(
                    result['amount'], result['category_name']))
            return transaction_breakdown
    except RuntimeError as e:
        print(e)
        raise ValueError('Cannot get transactions sum')


def get_transaction_by_id(transaction_id, user_id):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            query = f"select * from transactions where id={transaction_id} and is_deleted='false' and user_id={user_id}"
            cursor.execute(query)
            results = cursor.fetchall()
            transaction: list[Transaction] = []
            for result in results:
                transaction.append(Transaction(
                    result['id'], result['user_id'], result['vendor'], result['amount'], result['category_name'], result['is_deleted']))
            return transaction
    except RuntimeError as e:
        print(e)
        raise ValueError(
            f'Cannot get transaction id={transaction_id, user_id}')


def update_transactions(transaction: dict):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            update_transaction = f"update transactions set vendor = '{transaction['vendor']}', amount = {transaction['amount']} , category_name = '{transaction['category_name']}' where id = {transaction['id']}"
            cursor.execute(update_transaction)
            connection.commit()
            return Transaction(transaction['id'], transaction['user_id'], transaction['vendor'], transaction['amount'], transaction['category_name'])
    except RuntimeError as e:
        print(e)
        raise ValueError(f'Cannot update transaction')


def sum_deposits_by_category(user_id):
    try:
        connection.ping(reconnect=True)
        with connection.cursor() as cursor:
            sum_query = f"select SUM(amount) as amount, category_name from transactions where is_deleted='false' and user_id={user_id} and amount > 0 group by category_name"
            cursor.execute(sum_query)
            results = cursor.fetchall()
            transaction_breakdown: list[Transaction_Sum] = []
            for result in results:
                transaction_breakdown.append(Transaction_Sum(
                    result['amount'], result['category_name']))
            return transaction_breakdown
    except RuntimeError as e:
        print(e)
        raise ValueError('Cannot get transactions sum')
