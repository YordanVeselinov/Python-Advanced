def age_assignment(*args, **kwargs):
    result = ""
    for name in sorted(args):
        result += f"{name} is {kwargs[name[0]]} years old.\n"
    return result




print(age_assignment("Peter", "George", G=26, P=19))

# George is 26 years old.
# Peter is 19 years old.

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

# Amy is 22 years old.
# Bill is 61 years old.
# Willy is 36 years old.