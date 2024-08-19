def is_leap(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    return False

if __name__ == '__main__':
    year = int(input("Enter a year: "))
    if is_leap(year):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")
