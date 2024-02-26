n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
bombs_coordinates = [[int(x) for x in c.split(",")] for c in input().split()]

directions = (
    (-1, 0),   # up
    (1, 0),    # down
    (0, -1),   # left
    (0, 1),    # right
    (-1, 1),   # top-right
    (-1, -1),  # top-left
    (1, -1),   # bottom-left
    (1, 1),    # bottom-right
    (0, 0),    # current
)

for row, col in bombs_coordinates:
    if matrix[row][col] <= 0: # Checking if the bombs locations in greater than 0
        continue

    for x, y in directions: # Iterating though all the bombs radios(movement)
        r, c = x + row, y + col

        if 0 <= r < n and 0 <= c < n: # Checking if the movement(index) is in matrix
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0
            # Deducting the amount of the bomb if the current number is greater than 0


alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
# Finding all numbers in matrix that are greater than 0 (alive) and flattening them

print(f"Alive cells: {len(alive_cells)}")
print(f'Sum: {sum(alive_cells)}')

[print(*row) for row in matrix]
