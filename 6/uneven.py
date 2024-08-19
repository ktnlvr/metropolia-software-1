from random import randint, seed

def prune(ns: list[int]) -> list[int]:
    return [n for n in ns if n % 2 == 0]

if __name__ == '__main__':
    seed(8)
    integers = list(map(lambda _: randint(1, 100), range(10)))
    print(integers)
    print(prune(integers))
