from random import randint

def roll(n: int) -> int:
    return randint(1, n)

if __name__ == '__main__':
    rolls = 0
    while True:
        n = roll(6)
        print(n)
        rolls += 1
        if n == 6:
            break
