if __name__ == '__main__':
    cabin = input("Enter cabin class: ").strip()
    if cabin == "LUX":
        print("Upper-deck cabin with a balcony")
    elif cabin == "A":
        print("Above the car deck, equipped with a window")
    elif cabin == "B":
        print("Windowless cabin above the car deck")
    elif cabin == "C":
        print("Windowless cabin below the car deck")
    else:
        print("Invalid cabin class")