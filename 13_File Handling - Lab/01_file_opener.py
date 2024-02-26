import os


ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
file_name = "text_level2.txt"
path = os.path.join("..", "..", "Level 1", "Level 2", file_name)


try:
    file = os.path.join(path, file_name)
    print(file)
    print("File found")
except FileNotFoundError:
    print("File is not found")