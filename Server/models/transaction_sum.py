class Transaction_Sum():
    def __init__(self, amount_sum, category_name):
        self.amount_sum = amount_sum
        self.category_name = category_name

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
