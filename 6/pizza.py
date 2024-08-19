from math import pi

def price_per_unit(diameter: float, price: float) -> float:
    return (pi * (diameter / 2) ** 2) / price

if __name__ == "__main__":
    a_price = float(input("Enter price of first pizza: "))
    b_price = float(input("Enter price of second pizza: "))
    a_diameter = float(input("Enter diameter of first pizza: "))
    b_diameter = float(input("Enter diameter of second pizza: "))

    a_evaluation = price_per_unit(a_diameter, a_price)
    b_evaluation = price_per_unit(b_diameter, b_price)

    print("First pizza: ", a_evaluation, "area/cost")
    print("Second pizza: ", b_evaluation, "area/cost")

    if b_evaluation > a_evaluation:
        print("The second pizza is a better option")
    else:
        print("The first pizza is a better option")
