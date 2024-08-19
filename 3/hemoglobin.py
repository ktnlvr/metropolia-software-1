if __name__ == '__main__':
    sex = input("Enter your sex: ").lower().strip()
    hemoglobin = float(input("Enter your hemoglobin (g/l): "))
    if sex == "male" or sex == "m":
        if hemoglobin > 167:
            print("Hemoglobin above normal")
        elif hemoglobin < 134:
            print("Hemoglobin below normal")
        else:
            print("Hemoglobin normal")
    elif sex == "female" or sex == "f":
        if hemoglobin > 155:
            print("Hemoglobin above normal")
        elif hemoglobin < 117:
            print("Hemoglobin below normal")
        else:
            print("Hemoglobin normal")