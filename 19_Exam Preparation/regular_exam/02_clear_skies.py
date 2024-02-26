
size = int(input())
jet_fighter_position = None
matrix = []
initial_jet_armor = 300
enemies_jets = 0

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    current_row = list(input())

    if "J" in current_row:
        jet_fighter_position = [row, current_row.index("J")]
        current_row[jet_fighter_position[1]] = "-"

    enemies_jets += current_row.count('E')

    matrix.append(current_row)

while True:
    command = input()

    curr_row, curr_col = jet_fighter_position
    move_row, move_col = curr_row + direction_mapper[command][0], curr_col + direction_mapper[command][1]

    if not (0 <= move_row < size and 0 <= move_col < size):
        continue

    symbol = matrix[move_row][move_col]
    jet_fighter_position = [move_row, move_col]

    if symbol == "-":
        continue
    elif symbol == "R":
        matrix[move_row][move_col] = "-"
        initial_jet_armor = 300
    elif symbol == "E":
        matrix[move_row][move_col] = "-"
        enemies_jets -= 1
        initial_jet_armor -= 100

    if enemies_jets == 0:
        print(f"Mission accomplished, you neutralized the aerial threat!")
        break
    elif initial_jet_armor == 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{move_row}, {move_col}]!")
        break

matrix[jet_fighter_position[0]][jet_fighter_position[1]] = "J"

[print(*row,sep="") for row in matrix]