from collections import deque

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


size = int(input())
commands = deque(input().split(", "))
hazelnuts_collected = 0
matrix = []

squirrel_position = None

for row in range(size):
    line = list(input())

    if "s" in line:
        squirrel_position = [row, line.index("s")]

    matrix.append(line)

while commands:
    current_command = commands.popleft()
    row, col = squirrel_position
    move_row, move_col = row + direction_mapper[current_command][0], col + direction_mapper[current_command][1]

    if not (0 <= move_row < size and 0 <= move_col < size):
        print(f"The squirrel is out of the field.")
        break

    symbol = matrix[move_row][move_col]
    squirrel_position = [move_row, move_col]

    if symbol == "*":
        continue

    elif symbol == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    elif symbol == "h":
        matrix[move_row][move_col] = "*"
        hazelnuts_collected += 1

    if hazelnuts_collected >= 3:
        print(f"Good job! You have collected all hazelnuts!")
        break

else:
    print(f"There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")