if __name__ == '__main__':
    width = float(input("width = "))
    length = float(input("length = "))
    assert width >= 0
    assert length >= 0
    print(f"P = {2*width + 2*length}\tS = {width*length}")
