row, column = [int(x) for x in input().split(", ")]

matrix = []
sum_of_matrix = 0

for r in range(row):
    row_info = [int(x) for x in input().split(", ")]
    sum_of_matrix += sum(row_info)
    matrix.append(row_info)

print(sum_of_matrix)
print(matrix)

