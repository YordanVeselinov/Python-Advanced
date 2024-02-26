
try:
    text = input("Enter a random text: ")
    multiplier = int(input("Enter a multiplier: "))
    print(text * multiplier)
except ValueError:
    print(f"Variable times must be an integer")


