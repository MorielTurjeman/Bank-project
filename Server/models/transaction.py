class Transaction:
    def __init__(self, id, user_id, vendor, amount, category_name, is_deleted=False):

        self.id = id
        self.user_id = user_id
        self.vendor = vendor
        self.amount = amount
        self.category_name = category_name
        self.is_deleted = is_deleted

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
