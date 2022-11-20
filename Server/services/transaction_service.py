from models.transaction import Transaction
from data_accses_queries import transaction_data
from data_accses_queries import user_data
from exeptions.value_not_found_error import ValueNotFoundError
from services import user_service


# def add_transaction(transaction_from_user: transaction):
#     transaction_data.create_transaction(transaction_from_user)


def add_transaction(transaction: dict):
    transaction['user_id'] = user_service.get_logged_in_user()
    transaction['is_deleted'] = False
    t = transaction_data.create_transaction(transaction)
    user_service.update_balance(t.user_id, t.amount)
    print(t)
    return t


def delete_transaction(transaction_id):
    t = transaction_data.get_transaction_by_id(transaction_id)
    if t:
        transaction_data.delete_transaction(transaction_id)
        user_service.update_balance(t[0].user_id, t[0].amount*-1)
    else:
        raise ValueNotFoundError(
            f"Could not find transaction id {transaction_id}")


def get_transactions():
    transactions = transaction_data.get_transactions()
    return transactions


def get_transactions_by_category(category_name):
    transactions = transaction_data.get_transactions_by_category(category_name)
    return transactions


def sum_transactions_by_category():
    sum_transactions = transaction_data.sum_transactions_by_category()
    return sum_transactions