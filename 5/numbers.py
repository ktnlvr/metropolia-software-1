if __name__ == '__main__':
    numbers = []

    while inp := input("Enter a number: "):
        n = float(inp)
        numbers.append(n)
        numbers.sort(reverse=True)
        numbers = numbers[:5]

    for n in numbers:
        print(n)
