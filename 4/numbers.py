import math

if __name__ == '__main__':
    ma = -math.inf
    mi = +math.inf
    while inp := input("Enter a number: "):
        number = float(inp)
        ma = max(ma, number)
        mi = min(mi, number)
    print(f"min = {mi}\tmax = {ma}")
