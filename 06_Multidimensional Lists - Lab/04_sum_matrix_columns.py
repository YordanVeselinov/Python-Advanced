rows, col = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for i in range(rows)]

for col_index in range(col):
    current_col_sum = 0
    for row_index in range(rows):
        current_col_sum += matrix[row_index][col_index]
    print(current_col_sum)
