rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for i in range(rows)]

matches_counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_el = matrix[row][col]
        next_el = matrix[row][col + 1]
        down_el = matrix[row + 1][col]
        diagonal_el = matrix[row + 1][col + 1]
        if current_el == next_el == next_el == down_el == diagonal_el:
            matches_counter += 1

print(matches_counter)