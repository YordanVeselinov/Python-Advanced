class ValueCannotBeNegative(Exception):
    pass


class ValueCannotBeFloat(Exception):
    pass


try:
    n = int(input("How many number you want to enter: "))
    for _ in range(n):
        number = int(input())
        if number < 0:
            raise ValueCannotBeNegative("Number cannot be negative")

except ValueError:
    print(f'Invalid input!')
