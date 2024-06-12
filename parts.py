from factory import Factory


class Parts(Factory):
    def __init__(self, name, quantity):
        self.__name = name
        self._quantity = quantity

    def description(self):
        return f"Part: {self.__name}, Quantity: {self._quantity}"

    def validate(self):
        if not isinstance(self.__name, str):
            raise ValueError("Part name must be a string")
        if self._quantity <= 0:
            raise ValueError("Quantity must be positive")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity must be positive")
        self._quantity = value

    def __repr__(self):
        return self.description()

    def __str__(self):
        return self.description()
