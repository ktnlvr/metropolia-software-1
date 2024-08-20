from random import randint

if __name__ == '__main__':
    code1 = [randint(0, 9) for _ in range(3)]
    code2 = [randint(1, 6) for _ in range(4)]
    print(''.join(map(str, code1)))
    print(''.join(map(str, code2)))
