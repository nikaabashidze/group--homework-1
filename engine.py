from factory import Factory


class Engine(Factory):
    def __init__(self, type, horsepower):
        self.__type = type
        self._horsepower = horsepower

    def description(self):
        return f"Engine Type: {self.__type}, Horsepower: {self._horsepower} HP"

    def validate(self):
        if not isinstance(self.__type, str):
            raise ValueError("Engine type must be a string")
        if self._horsepower <= 0:
            raise ValueError("Horsepower must be positive")

    @property
    def horsepower(self):
        return self._horsepower

    @horsepower.setter
    def horsepower(self, value):
        if value <= 0:
            raise ValueError("Horsepower must be positive")
        self._horsepower = value

    def __repr__(self):
        return self.description()

    def __str__(self):
        return self.description()
