r, c = [int(x) for x in input().split()]

matrix = [[int(z) for z in input().split()] for x in range(r)]

while True:
    command, *data = input().split()

    if command == "END":
        break

    if len(data) > 4 or len(data) < 4 or command != "swap":
        print(f"Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in data]

    if not (0 <= row1 < r and 0 <= col1 < c and 0 <= row2 < r and 0 <= col2 < c):
        print(f"Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=" ")
