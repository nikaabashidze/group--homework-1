from factory import Factory


class Vehicle(Factory):
    def __init__(self, name, engine, parts, design):
        self.__name = name
        self.engine = engine
        self.parts = parts
        self.design = design

    def description(self):
        return f"Vehicle: {self.__name}, Engine: {self.engine}, Parts: {self.parts}, Design: {self.design}"

    def validate(self):
        if not isinstance(self.__name, str):
            raise ValueError("Name must be a string")
        if len(self.__name) < 3:
            raise ValueError("Name must be at least 3 characters long")

    def __repr__(self):
        return self.description()

    def __str__(self):
        return self.description()
