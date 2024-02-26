size = int(input())

matrix = []
bunny_pos = []
max_collected_eggs = float("-inf")
best_direction = ""
positions = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(size):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

for direction, coordination in directions.items():
    r, c = bunny_pos[0] + coordination[0], bunny_pos[1] + coordination[1]
    current_max = 0
    current_movements = []
    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "X":
            break

        if matrix[r][c].isdigit():
            current_max += int(matrix[r][c])
            current_movements.append([r, c])

        r += coordination[0]
        c += coordination[1]
    if current_max >= max_collected_eggs:
        max_collected_eggs = current_max
        best_direction = direction
        positions = current_movements

print(best_direction)
[print(row) for row in positions]
print(max_collected_eggs)