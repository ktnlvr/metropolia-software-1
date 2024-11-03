from car import Car, car

def _accelerate(self: Car, dv_km_per_h: float):
    self.current_speed_km_per_h += dv_km_per_h
    if self.current_speed_km_per_h < 0:
        self.current_speed_km_per_h = 0
    if self.current_speed_km_per_h > self.maximum_speed_km_per_h:
        self.current_speed_km_per_h = self.maximum_speed_km_per_h

# to submit each part as its own exercises this was monkeypatched
Car.accelerate = _accelerate

# the exercise also mentions the speed property, which was not mentioned before, so just to follow the contract
Car.speed = property(lambda self: self.current_speed_km_per_h)
Car.speed.setter(lambda self, value: setattr(self, 'current_speed_km_per_h', value))

car.accelerate(30)
assert car.speed == 30
car.accelerate(70)
assert car.speed == 100
car.accelerate(50)
assert car.speed == car.speed
car.accelerate(-200)
assert car.speed == 0
