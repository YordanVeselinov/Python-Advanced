import os

while True:
    command, *data = input().split("-")

    if command == "Create":
        file_name = data[0]
        with open(f"resources/ex_03/{file_name}", "w"):
            pass

    elif command == "Add":
        file_name, content = data[0], data[1]
        with open(f"resources/ex_03/{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        try:
            file_name, old_string, new_string = data[0], data[1], data[2]
            with open(f"resources/ex_03/{file_name}", "r+") as file:
                text = file.read()
                text = text.replace(old_string, new_string)

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "Delete":
        try:
            os.remove(f"resources/ex_03/{data[0]}")
        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "End":
        break
