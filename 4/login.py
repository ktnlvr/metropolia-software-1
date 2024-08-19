from getpass import getpass as input_password

if __name__ == '__main__':
    username = None
    password = None
    attempts_left = 5
    while attempts_left > 0:
        username = input("Username: ")
        password = input_password("Password: ")
        attempts_left -= 1
        if username == "python" and password == "rules":
            break
    else:
        print("Access denied")
        exit(-1)
    print("Welcome")
