# TIL: python does not allow numeric module names
# this is a reimplementation of ../9/car.py
# since using importlib seems overkill for this exercise
#
# I am avoiding code reuse,
# which is a shame,
# but I guess it isn't a criteria here
from random import random
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, registration: str, maximum_speed_km_per_h: float):
        self.registration = registration
        self.maximum_speed_km_per_h = maximum_speed_km_per_h
        self.travelled_distance_km = 0.
        self.current_speed_km_per_h = 0.

    def drive(self, h: float):
        self.travelled_distance_km += self.current_speed_km_per_h * h

    def accelerate(self, dv_km_per_h: float):
        self.current_speed_km_per_h += dv_km_per_h
        if self.current_speed_km_per_h < 0:
            self.current_speed_km_per_h = 0
        if self.current_speed_km_per_h > self.maximum_speed_km_per_h:
            self.current_speed_km_per_h = self.maximum_speed_km_per_h

    @abstractmethod
    def __str__(self):
        ...

class ElectricCar(Car):
    def __init__(self, registration: str, max_speed_km_per_h: float, battery_capacity_kw_h: float):
        super().__init__(registration, max_speed_km_per_h)
        self.battery_capacity_kw_h = battery_capacity_kw_h

    def __str__(self):
        return f"({self.registration}, {round(self.maximum_speed_km_per_h)} km/h, {self.battery_capacity_kw_h:.4} kWh)"

class GasolineCar(Car):
    def __init__(self, registration: str, max_speed_km_per_h: float, tank_volume_l: float):
        super().__init__(registration, max_speed_km_per_h)
        self.tank_volume_l = tank_volume_l

    def __str__(self):
        return f"({self.registration}, {round(self.maximum_speed_km_per_h)} km/h, {self.tank_volume_l:.4} l)"

if __name__ == "__main__":
    gas = GasolineCar("GAS-556", 300., 88.)
    zap = ElectricCar("ZAP-665", 120., 20.)

    cars = [gas, zap]

    for car in cars:
        car.accelerate(random() * 110)
        car.drive(3)
        print(f"{car} travelled {car.travelled_distance_km} km")
