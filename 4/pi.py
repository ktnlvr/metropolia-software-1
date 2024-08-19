from random import random, seed

if __name__ == "__main__":
    iterations = int(input("Enter amount of iterations: ") or "0") or 1_000_000_000
    seed(int(input("Enter seed: ") or "0"))

    total = 0
    inside = 0
    for i in range(iterations):
        total += 1
        if random()**2 + random()**2 < 1:
            inside += 1
    approx = 4 * inside / total
    print(f"π ≈ {approx}")

    # I added the following piece just for the sake of it
    # not part of the exercise

    from math import pi
    for i, (a, b) in enumerate(zip(str(approx)[2:], str(pi)[2:])):
        if a != b:
            break
    i += 2
    print("approx: ", str(approx)[:i], str(approx)[i:])
    print("pi:     ", str(pi)[:i], str(pi)[i:]  )
    print(f"correct up to {i} digits")
