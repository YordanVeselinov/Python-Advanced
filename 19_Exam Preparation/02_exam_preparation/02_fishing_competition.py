size = int(input())


FISH_TO_REACH = 20
matrix = []
position = None
collected_fish = 0

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = list(input())

    if "S" in line:
        position = [row, line.index("S")]
        line[position[1]] = "-"
    matrix.append(line)


command = input()

while command != "collect the nets":
    curr_row, curr_col = position
    move_row, move_col = curr_row + direction_mapper[command][0], curr_col + direction_mapper[command][1]

    move_row = (move_row + size) % size
    move_col = (move_col + size) % size

    symbol = matrix[move_row][move_col]
    position = [move_row, move_col]

    if symbol == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{move_row},{move_col}]")
        exit()
    elif symbol.isdigit():
        collected_fish += int(symbol)
        matrix[move_row][move_col] = '-'

    command = input()

matrix[position[0]][position[1]] = "S"

if collected_fish >= FISH_TO_REACH:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {FISH_TO_REACH - collected_fish} tons of fish more.")

if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(*row,sep="") for row in matrix]