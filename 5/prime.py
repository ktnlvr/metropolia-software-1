from math import sqrt

if __name__ == '__main__':
    n = int(input("Enter a number: "))

    is_prime = True
    factors = (None, None)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            factors = (i, n // i)
            break

    if is_prime:
        print(f"{n} is prime")
    else:
        a, b = factors
        print(f"{n} is not prime ({a} * {b} = {n})")
