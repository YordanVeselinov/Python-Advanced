n = int(input())

commands = input().split()

matrix = []
miner_position = []

total_coal, collected_coal = 0, 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(n):  # Creating the matrix
    matrix.append(input().split())

    if "s" in matrix[row]:
        # Finding the miner's location and also removing him from the matrix
        miner_position = [row, matrix[row].index("s")]
        matrix[miner_position[0]][miner_position[1]] = "*"

    # Counting all the coil in the matrix
    total_coal += matrix[row].count("c")

for command in commands:
    r, c = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_position = [r, c]
    # Moving miners position

    if matrix[r][c] == "c":
        # Checking if miner found coil and adding it to collected_coil
        collected_coal += 1

        if collected_coal == total_coal:
            # Checking if miner found all the coils in matrix if so we end the game
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == "e":
        # Checking if miner step on E and the game is over
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"

# If miner didn't find all the coin and didn't step on E
# we print the amount of coil he collected and his position
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
