number = int(input("Enter number:  "))


def calculate(number):
    if number < 0:
        return -number
    elif number > 0:
        return number
    else:
        return 0
print(calculate(number))