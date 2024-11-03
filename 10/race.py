from random import random

# since the folders are named numerically, doing a complete relative
# import is too much hustle, so I Ctrl+C Ctrl+Ved the source here

class Car:
    def __init__(self, registration: str, maximum_speed_km_per_h: float):
        self.registration = registration
        self.maximum_speed_km_per_h = float(maximum_speed_km_per_h)
        self.current_speed_km_per_h = 0.
        self.travelled_distance_km = 0.

    def __str__(self) -> str:
        return f"({self.registration}, {round(self.maximum_speed_km_per_h)} km/h)"

    def drive(self, hours: float):
        self.travelled_distance_km += hours * self.current_speed_km_per_h

    def accelerate(self, dv_km_per_h: float):
        self.current_speed_km_per_h += dv_km_per_h
        if self.current_speed_km_per_h < 0:
            self.current_speed_km_per_h = 0
        if self.current_speed_km_per_h > self.maximum_speed_km_per_h:
            self.current_speed_km_per_h = self.maximum_speed_km_per_h

class Race:
    def __init__(self, name: str, distance_km: float, cars: list[Car]):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

        for car in self.cars:
            assert car.travelled_distance_km == 0

    def hour_passes(self):
        for car in self.cars:
            acc = random() * 82 - 2.
            car.accelerate(acc)
            car.drive(1)

    def print_status(self):
        participants = self.cars

        max_car_registration_len = max(map(lambda c: len(c.registration), participants))
        max_speed_len = max(map(lambda c: len(str(c.maximum_speed_km_per_h)), participants))
        max_speed_len = max(max_speed_len, len("max speed"))
        max_travelled_distance_len = max(map(lambda c: len(str(c.travelled_distance_km)), participants))
        fmt = f"| {{:<{max_car_registration_len}}} | {{:{max_speed_len}}} | {{:{max_travelled_distance_len}}} |"

        # not printing out anything else, since the current speed is not really a car parameter
        print(fmt.format("no", "max speed", "travelled distance"))
        print(fmt.format("-" * max_car_registration_len, "-" * max_speed_len, "-" * max_travelled_distance_len))
        for c in participants:
            print(fmt.format(c.registration, c.maximum_speed_km_per_h, c.travelled_distance_km))

    def race_finished(self):
        return any([car.travelled_distance_km >= self.distance_km for car in self.cars])

if __name__ == "__main__":
    crazy_car = Car("CrAzY cAr =)", 150)
    calmer_car = Car("calmer car :)", 120)
    happy_car = Car("happy car :D", 100)
    new_car = Car("new car ;)", 130)
    old_car = Car("old car ;]", 30)

    cars = [crazy_car, calmer_car, happy_car, new_car, old_car]
    for i in range(10 - len(cars)):
        cars.append(Car(f"Random Car {i}", random() * 90 + 10.))

    race = Race("Grand Demolition Derby", 8000, cars)

    h = 0
    while not race.race_finished():
        race.hour_passes()
        h += 1
        if h % 10 == 0:
            print(f"Hour {h}")
            race.print_status()
    print(f"Hour {h}! Race finished!")
    race.print_status()
