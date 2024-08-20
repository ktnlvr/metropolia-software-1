class Car:
    def __init__(self, registration: str, maximum_speed_km_per_h: float):
        self.registration = registration
        self.maximum_speed_km_per_h = float(maximum_speed_km_per_h)
        self.current_speed_km_per_h = 0.
        self.travelled_distance_km = 0.

    def __str__(self) -> str:
        return f"({self.registration}, {round(self.maximum_speed_km_per_h)} km/h)"

car = Car("ABC-123", 142)

if __name__ == "__main__":
    print(car)
