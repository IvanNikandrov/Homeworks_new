from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 1500
    started = False
    fuel = 50
    fuel_consumption = 10

    def __init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if max_distance >= distance:
            self.fuel -= int(distance * self.fuel_consumption)
        else:
            raise NotEnoughFuel


