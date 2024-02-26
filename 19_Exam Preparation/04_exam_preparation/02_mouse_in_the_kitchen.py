rows, cols = [int(x) for x in input().split(",")]
cupboard = []
mouse_position = None
all_cheeses = 0
ate_cheeses = 0

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    line = list(input())

    if "M" in line:
        mouse_position = [row, line.index("M")]
    all_cheeses += line.count("C")
    cupboard.append(line)

command = input()

while command != "danger":
    current_pos_row, current_pos_col = mouse_position
    move_row, move_col = current_pos_row + direction_mapper[command][0], current_pos_col + direction_mapper[command][1]

    if not (0 <= move_row < rows and 0 <= move_col < cols):
        print(f"No more cheese for tonight!")
        break

    symbol = cupboard[move_row][move_col]

    if symbol == "@":
        command = input()
        continue

    elif symbol == "T":
        cupboard[current_pos_row][current_pos_col] = "*"
        cupboard[move_row][move_col] = "M"

        print(f"Mouse is trapped!")
        break

    elif symbol == "C":
        ate_cheeses += 1
        cupboard[current_pos_row][current_pos_col] = "*"
        cupboard[move_row][move_col] = "M"
        mouse_position = [move_row, move_col]

        if ate_cheeses == all_cheeses:
            print(f"Happy mouse! All the cheese is eaten, good night!")
            break
    elif symbol == "*":
        cupboard[current_pos_row][current_pos_col] = "*"
        cupboard[move_row][move_col] = "M"
        mouse_position = [move_row, move_col]

    command = input()

else:
    print(f"Mouse will come back later!")



[print(*row, sep="") for row in cupboard]

# print(all_cheeses)
# print(mouse_position)
# print(*cupboard, sep="\n")