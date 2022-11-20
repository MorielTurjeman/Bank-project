class User:
    def __init__(self, id, first_name, last_name, current_balance) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.current_balance = current_balance

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()
