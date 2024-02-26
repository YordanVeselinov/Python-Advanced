import os

path = os.path.join("Level 1", "Level 2", "text_level2.txt")

try:
    os.remove(path)
except FileNotFoundError:
    print("File is already deleted")

