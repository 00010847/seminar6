number = int(input("Enter number:  "))


def calculate(x, y):
    if x < y:
        return 1
    elif x > y:
        return number
    else:
        return 0
print(calculate(number))