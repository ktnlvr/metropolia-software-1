def gal_to_l(n: float) -> float:
    return n * 4.54609


if __name__ == '__main__':
    while (n := float(input("Enter quantity of gasoline in gallons: "))) >= 0:
        print(f"{n} gallons = {gal_to_l(n)} litres")