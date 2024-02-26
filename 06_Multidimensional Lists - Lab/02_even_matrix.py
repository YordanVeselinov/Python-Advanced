# Solution 1
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for i in range(int(input()))]

print(matrix)

# # Solution 2
# matrix = []
#
# for r in range(int(input())):
#     matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
#
# print(matrix)
#
# # Solution 3
# matrix = []
#
# for r in range(int(input())):
#     row_data = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
#     matrix.append(row_data)
#
# print(matrix)
