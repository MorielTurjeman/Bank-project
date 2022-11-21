class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if (isinstance(other, Category)):
            return self.name == other.name
        elif (isinstance(other, str)):
            return self.name == other

        return False
