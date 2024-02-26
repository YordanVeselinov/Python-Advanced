rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]

primary = [matrix[index][index] for index in range(rows)]
secondary = [matrix[row_index][rows - 1 - row_index] for row_index in range(rows)]

# for index in range(rows):
#     primary.append(matrix[index][index])

# for row_index in range(rows):
#     secondary.append(matrix[row_index][rows - 1 - row_index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")
