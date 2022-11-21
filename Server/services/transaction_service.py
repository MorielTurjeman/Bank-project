from models.transaction import Transaction
from data_accses_queries import transaction_data
from data_accses_queries import user_data
from exeptions.value_not_found_error import ValueNotFoundError
from services import user_service


# def add_transaction(transaction_from_user: transaction):
#     transaction_data.create_transaction(transaction_from_user)


def add_transaction(transaction: dict, user_id):
    transaction['user_id'] = user_id
    transaction['is_deleted'] = False
    new_transaction = transaction_data.create_transaction(transaction)
    user_service.update_balance(
        new_transaction.user_id, new_transaction.amount)
    print(new_transaction)
    return new_transaction


def delete_transaction(transaction_id, user_id):
    transaction = transaction_data.get_transaction_by_id(
        transaction_id, user_id)
    if transaction:
        transaction_data.delete_transaction(transaction_id, user_id)
        user_service.update_balance(
            transaction[0].user_id, transaction[0].amount*-1)
    else:
        raise ValueNotFoundError(
            f"Could not find transaction id {transaction_id}")


def get_transactions(user_id):
    transactions = transaction_data.get_transactions(user_id)
    return transactions


def get_transactions_by_category(category_name, user_id):
    transactions = transaction_data.get_transactions_by_category(
        category_name, user_id)
    return transactions


def sum_transactions_by_category(user_id):
    sum_transactions = transaction_data.sum_transactions_by_category(user_id)
    return sum_transactions
