import math

from drive import Car
from random import random

FINISH_LINE_KM = 10_000
RACERS = 10
ITERS = 10000

def race(racers: int, early_exit: bool = True) -> tuple[list[Car], list[Car]]:
    assert racers > 0

    cars = [Car(f"ABC-{i+1}", random() * 100 + 100) for i in range(racers)]

    candidates = set()
    while not candidates:
        for car in cars:
            car.accelerate(25. * random() - 10.)

            time_to_finish = 0
            if car.current_speed_km_per_h != 0:
                time_to_finish = (FINISH_LINE_KM - car.travelled_distance_km) / car.current_speed_km_per_h

            car.drive(1)

            if car.travelled_distance_km >= FINISH_LINE_KM:
                if early_exit:
                    return ([car], cars)
                else:
                    candidates.add((time_to_finish, car))
    lowest_time = math.inf
    winners = []
    for time, car in candidates:
        if time == lowest_time:
            winners.append(car)
        if time < lowest_time:
            winners = [car]
    return winners, cars

def simulate():
    results = list(map(lambda _: 0, range(RACERS)))

    for x in range(ITERS):
        print(f"{x/ITERS:.2}")

        # If `early_exit` is enabled the race will stop when the first candidate finished
        # This makes the race inaccurate and gives advantages to racers with lesser car numbers
        # since it is possible for the racers to finish at the same time
        # If `early_exit` is disabled, the race has a "photofinish" system
        # which works by measuring the amount of time required for each car to have reached
        # the finish line from their distance before accelerating
        for car in race(RACERS, False)[0]:
            print(car)
            car_no = int(car.registration[4:])
            results[car_no - 1] += 1

    print(results)

def main():
    winners, participants = race(RACERS, False)
    if len(winners) == 1:
        print(f"Car {winners[0].registration} is the winner")
    else:
        lhs, rhs = winners[:-1], winners[-1]
        print("Tie between cars", ', '.join(map(lambda c: c.registration, lhs)), "and", rhs.registration)
    print("All participants:")

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

if __name__ == '__main__':
    from os import environ

    # set the environmental variable and simulate multiple runs!
    if environ.get("SIMULATE_RACE"):
        simulate()
    else:
        main()
