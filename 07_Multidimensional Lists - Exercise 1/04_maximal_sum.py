rows, cols = [int(x) for x in input().split()]

matrix = [[int(y) for y in input().split()] for x in range(rows)]

max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]
        sum_of_sub_matrix = sum(first_row) + sum(second_row) + sum(third_row)
        if sum_of_sub_matrix > max_sum:
            max_sum = sum_of_sub_matrix
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
for row in sub_matrix:
    print(*row, sep=" ")