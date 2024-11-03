from elevator import Elevator

class Building:
    def __init__(self, bottom: int, top: int, elevator_count: int):
        self.elevators = [Elevator(bottom, top) for _ in range(elevator_count)]

    def run_elevator(self, idx: int, floor: int):
        self.elevators[idx].go_to_floor(floor + 1)

if __name__ == "__main__":
    N = 4
    b = Building(1, 5, N)
    for n in range(N):
        b.run_elevator(n, n)
