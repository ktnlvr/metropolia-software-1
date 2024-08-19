if __name__ == '__main__':
    a, b, c = map(lambda i: float(input(f"x{i} = ")), range(3))
    print(f"sum = {a+b+c}\tproduct = {a * b * c}\taverage = {(a+b+c)/3}")