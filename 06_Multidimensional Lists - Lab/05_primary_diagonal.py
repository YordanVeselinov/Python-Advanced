size_square_matrix = int(input())

matrix = [[int(z) for z in input().split()] for x in range(size_square_matrix)]

sum_diagonal = 0

for row_index in range(size_square_matrix):
    for col_index in range(size_square_matrix):
        if row_index == col_index:
            sum_diagonal += matrix[row_index][col_index]

print(sum_diagonal)