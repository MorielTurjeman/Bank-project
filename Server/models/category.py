class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.__str__()
