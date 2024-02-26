rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(z) for z in input().split(", ")] for i in range(rows)]

sub_matrix = []
max_sum = float('-inf')

for row_index in range(rows - 1):
    for col_index in range(cols - 1):

        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        down_el = matrix[row_index+1][col_index]
        diagonal_el = matrix[row_index+1][col_index+1]
        sum_of_current = current_el + next_el + down_el + diagonal_el

        if sum_of_current > max_sum:
            max_sum = sum_of_current
            sub_matrix = [[current_el, next_el], [down_el, diagonal_el]]

# for row in sub_matrix:
#     print(*row, sep=" ")
print(*sub_matrix[0])
print(*sub_matrix[1])

print(max_sum)