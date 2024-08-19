if __name__ == '__main__':
    names = set()
    while name := input("Enter a name: "):
        if name not in names:
            print("New name")
            names |= {name}
        else:
            print("Existing name")

    for name in names:
        print(name)