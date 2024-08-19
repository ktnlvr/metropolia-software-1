if __name__ == '__main__':
    length = float(input("Length of the zander (cm): "))
    size_limit = 42
    if length < size_limit:
        print("Release the zander.")
        print(f"The zander is {size_limit - length:.5} cm below the size limit.")
    else:
        print("The zander is fine, good catch.")
