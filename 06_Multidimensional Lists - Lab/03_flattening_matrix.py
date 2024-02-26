# Solution 1
matrix = [[int(x) for x in input().split(", ")]for x in range(int(input()))]

print([el for row in matrix for el in row])

# Solution 2
# row = int(input())
#
# matrix = []
# flatten_matrix = []
#
# for row in range(row):
#     matrix.append([int(x) for x in input().split(", ")])
#
# for row in matrix:
#     for el in row:
#         flatten_matrix.append(el)
#
# print(flatten_matrix)