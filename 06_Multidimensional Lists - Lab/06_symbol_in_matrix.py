row = int(input())

matrix = [[y for y in input()] for x in range(row)]
element_to_find = input()


for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == element_to_find:
            print(f"({row_index}, {col_index})")
            exit()


print(f"{element_to_find} does not occur in the matrix")
