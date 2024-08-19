from car import Car, car

def _accelerate(self: Car, dv_km_per_h: float):
    self.current_speed_km_h += dv_km_per_h
    if self.current_speed_km_h < 0:
        self.current_speed_km_h = 0
    if self.current_speed_km_h > self.maximum_speed_km_per_h:
        self.current_speed_km_h = self.maximum_speed_km_per_h

Car.accelerate = _accelerate

car.accelerate(30)
assert car.current_speed_km_h == 30
car.accelerate(70)
assert car.current_speed_km_h == 100
car.accelerate(50)
assert car.current_speed_km_h == car.maximum_speed_km_per_h
car.accelerate(-200)
assert car.current_speed_km_h == 0
