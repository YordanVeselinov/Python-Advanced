with open("my_first_file.txt", "a") as file:
    file.write("I just created my first file!")

file = open("test.txt", "a")
file.write("Hello \n")

file.write('Hello\n')

file.close()