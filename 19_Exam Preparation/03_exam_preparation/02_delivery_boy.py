rows, cols = [int(x) for x in input().split()]

field = []
delivery_boy_position = None
starting_position = None

for row in range(rows):
    line = list(input())

    if "B" in line:
        delivery_boy_position = [row, line.index("B")]
        starting_position = delivery_boy_position.copy()

    field.append(line)

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    row, col = delivery_boy_position
    move_row, move_col = row + direction_mapper[command][0], col + direction_mapper[command][1]

    if not (0 <= move_row < rows and 0 <= move_col < cols):
        field[starting_position[0]][starting_position[1]] = " "
        print(f"The delivery is late. Order is canceled.")
        break

    symbol = field[move_row][move_col]

    if symbol == "*":
        continue

    delivery_boy_position = [move_row, move_col]

    if symbol == "P":
        field[move_row][move_col] = "R"
        print(f"Pizza is collected. 10 minutes for delivery.")

    elif symbol == "A":
        field[move_row][move_col] = "P"
        print(f'Pizza is delivered on time! Next order...')
        break

    elif symbol == "-":
        field[move_row][move_col] = "."

[print(*current_row, sep="") for current_row in field]
