from random import randint as rnd

if __name__ == '__main__':
    number = rnd(1, 10)
    guess = None
    while guess != number:
        guess = int(input("Enter guess: "))
        if number > guess:
            print("Too low")
        elif number < guess:
            print("Too high")
    print("Correct!")
