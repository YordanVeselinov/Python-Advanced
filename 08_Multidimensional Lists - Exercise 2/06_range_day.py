size = 5

matrix = []
position = []
target_shot = 0
all_targets = 0
targets_locations = []


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(size):
    matrix.append(input().split())

    if "A" in matrix[row]:
        position = [row, matrix[row].index("A")]

    all_targets += matrix[row].count("x")

for _ in range(int(input())):
    command = input().split()

    if command[0] == "move":
        direction, multiplier = command[1], int(command[2])
        r, c = position[0] + (directions[direction][0] * multiplier), position[1] + (directions[direction][1] * multiplier)
        if 0 <= r < size and 0 <= c < size and matrix[r][c] == ".":
            position = [r, c]
        else:
            continue
    elif command[0] == "shoot":
        direction = command[1]
        r, c = position[0] + directions[direction][0], + position[1] + directions[direction][1]
        while 0 <= r < size and 0 <= c < size:
            if matrix[r][c] == "x":
                target_shot += 1
                targets_locations.append([r, c])
                matrix[r][c] = "."
                break
            r += directions[direction][0]
            c += directions[direction][1]
        if target_shot == all_targets:
            print(f"Training completed! All {all_targets} targets hit.")
            break


if target_shot < all_targets:
    print(f"Training not completed! {all_targets - target_shot} targets left.")

[print(row) for row in targets_locations]
