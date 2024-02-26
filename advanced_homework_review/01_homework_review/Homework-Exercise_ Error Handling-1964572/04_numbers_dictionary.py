numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
        line = input()
    except ValueError:
        print("The variable number must be an integer")
        line = input()
        continue

line = input()
while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
        line = input()
    except KeyError:
        print("Number does not exist in dictionary")
        line = input()
        continue

line = input()
while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
        line = input()
    except KeyError:
        print("Number does not exist in dictionary")
        line = input()
        continue

print(numbers_dictionary)
