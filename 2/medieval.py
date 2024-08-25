if __name__ == '__main__':
    talents = float(input("Enter talent: "))
    pounds = float(input("Enter pounds: "))
    lots = float(input("Enter lots: "))

    pounds += talents * 20
    lots += pounds * 32
    grams = lots * 13.3
    kg = int(grams / 1000)
    g = grams - kg * 1000

    print("The weight in modern units:")
    print(f"{kg} kilograms and {g:.2f} grams.")
