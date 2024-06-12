from factory import Factory


class Design(Factory):
    def __init__(self, style, color):
        self.__style = style
        self.__color = color

    def description(self):
        return f"Design Style: {self.__style}, Color: {self.__color}"

    def validate(self):
        if not isinstance(self.__style, str):
            raise ValueError("Style must be a string")
        if not isinstance(self.__color, str):
            raise ValueError("Color must be a string")

    def __repr__(self):
        return self.description()

    def __str__(self):
        return self.description()
