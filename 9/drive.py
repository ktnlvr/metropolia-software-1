from accelerate import Car, car

def _drive(self: Car, h: float):
    self.travelled_distance_km += h * self.current_speed_km_per_h

Car.drive = _drive

car.travelled_distance_km = 2000
car.current_speed_km_per_h = 60
car.drive(1.5)
assert car.travelled_distance_km == 2090
