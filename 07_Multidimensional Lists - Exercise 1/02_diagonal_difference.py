# Solution 1
# rows = int(input())
#
# matrix = [[int(x) for x in input().split()] for i in range(rows)]
#
# primary, secondary = 0, 0
#
# for index in range(rows):
#     primary += matrix[index][index]
#     secondary += matrix[index][rows - 1 - index]
#
# print(abs(primary - secondary))

# Solution 2
rows = int(input())

primary, secondary = 0, 0

for index in range(rows):
    line = [int(x) for x in input().split()]
    primary += line[index]
    secondary += line[rows - 1 - index]

print(abs(primary - secondary))
