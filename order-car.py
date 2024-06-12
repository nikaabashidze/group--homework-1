from vehicle import Vehicle
from engine import Engine
from parts import Parts
from design import Design
from mixin import LogMixin


class Car(Vehicle, LogMixin):
    def __init__(self, name, engine, parts, design):
        super().__init__(name, engine, parts, design)
        self.log("Car initialized")

    def additional_method(self):
        self.log("Additional method called")


engine = Engine("V8", 450)
engine.validate()

parts = Parts("Wheel", 4)
parts.validate()

design = Design("Sedan", "Red")
design.validate()

car = Car("Mustang", engine, parts, design)
print(car)
car.additional_method()
