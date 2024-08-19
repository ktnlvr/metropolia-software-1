from random import randint

if __name__ == '__main__':
    n = int(input("How many dice to roll? "))
    total = 0
    for i in range(n):
        total += randint(1, 6)
    print(total)
