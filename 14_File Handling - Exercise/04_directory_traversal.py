import os


def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        current_file = os.path.join(dir_name, filename)

        if os.path.isfile(current_file):
            file_extension = filename.split(".")[-1]
            extensions[file_extension] = extensions.get(file_extension, []) + [filename]
        elif os.path.isdir(current_file):
            save_extensions(current_file)


while True:
    directory = './' + input("Enter a directory: ")
    extensions = {}  # [py: [python.py, hello.py], ...}
    output = []

    try:
        save_extensions(directory)
        break
    except FileNotFoundError:
        print("Directory not found!")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    output.append(f".{extension}")

    for file in sorted(files):
        output.append(f"- - - {file}")

with open("resources/ex_04/report_04.txt", "w") as report_file:
    report_file.write('\n'.join(output))
