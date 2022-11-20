from exeptions.value_not_found_error import ValueNotFoundError
from data_accses_queries import user_data


# Since we dont support login or multiple users in the UI, this method always return 1 (the only exiesing user).
# In the future, when multiple users will be supported, I will update the function to reutn the actual logged in user.
def get_logged_in_user():
    return 1


def get_balance(user_id):
    user_balance = user_data.get_balance(user_id)
    if user_balance:
        return user_balance[0]
    else:
        raise ValueNotFoundError(
            f"Could not find user id {user_id}")


def update_balance(user_id, amount):
    user_data.update_balance(user_id, amount)


# def update_balance(user_id, amount):
#     user_data.update_balance(get_logged_in_user(), amount)
