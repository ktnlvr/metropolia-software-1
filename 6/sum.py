from random import randint

def total(ints: list[int]) -> int:
    acc = 0
    for i in ints:
        acc += i
    return acc

if __name__ == '__main__':
    integers = list(map(lambda x: randint(x, 2*x), range(100)))
    n = total(integers)
    assert sum(integers) == n
    print(n)
