from building import Building

def _fire_alarm(self: Building):
    print("Boop boop, fire alarm!")
    for elevator in self.elevators:
        elevator.go_to_floor(elevator.bottom)

Building.fire_alarm = _fire_alarm

if __name__ == "__main__":
    N = 3
    b = Building(1, 5, N)
    for n in range(N):
        b.run_elevator(n, n + 1)
    print("-" * 10)
    b.fire_alarm()
