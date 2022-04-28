"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 1000
    def __init__(self, weight, fuel, fuel_consumption, max_cargo=max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, digit: int):
        current_cargo = self.cargo + digit
        if current_cargo <= self.max_cargo:
            self.cargo = current_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo

