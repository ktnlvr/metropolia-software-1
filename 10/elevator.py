class Elevator:
    def __init__(self, bottom: int, top: int):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def go_to_floor(self, n: int):
        print(f"Going from {self.current_floor} to {n}")
        assert n <= self.top
        assert n >= self.bottom
        d = n - self.current_floor
        for i in range(abs(d)):
            if d < 0:
                self.floor_down()
            else:
                self.floor_up()
        print(f"Ding, reached {n}")

    def floor_up(self):
        print(f"Going up from {self.current_floor} to {self.current_floor + 1}")
        self.current_floor += 1

    def floor_down(self):
        print(f"Going down from {self.current_floor} to {self.current_floor - 1}")
        self.current_floor -= 1

if __name__ == "__main__":
    h = Elevator(bottom=1, top=5)
    h.go_to_floor(5)
    assert h.current_floor == 5
