from dice import roll

if __name__ == '__main__':
    power = int(input("Enter amount of sides: "))
    rolls = 0
    while True:
        n = roll(power)
        print(n)
        rolls += 1
        if n == power:
            break
