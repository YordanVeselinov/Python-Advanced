
size = int(input())
gambler_position = None
current_amount = 100
jackpot = False

matrix = []

direction_map = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


for row in range(size):
    line = list(input())

    if "G" in line:
        gambler_position = [row, line.index("G")]
        line[gambler_position[1]] = "-"

    matrix.append(line)


command = input()

while command != "end":
    row, col = gambler_position
    move_row, move_col = row + direction_map[command][0], col + direction_map[command][1]

    if not (0 <= move_row < size and 0 <= move_col < size):
        print(f"Game over! You lost everything!")
        exit()

    symbol = matrix[move_row][move_col]
    matrix[move_row][move_col] = "-"
    gambler_position = [move_row, move_col]

    if symbol == "W":
        current_amount += 100
    elif symbol == "J":
        current_amount += 100000
        jackpot = True
        break
    elif symbol == "P":
        current_amount -= 200

    if current_amount <= 0:
        print(f"Game over! You lost everything!")
        exit()

    command = input()

matrix[gambler_position[0]][gambler_position[1]] = "G"

if jackpot:
    print(f"You win the Jackpot! End of the game. Total amount: {current_amount}$")
else:
    print(f"End of the game. Total amount: {current_amount}$")

[print(*row, sep="") for row in matrix]