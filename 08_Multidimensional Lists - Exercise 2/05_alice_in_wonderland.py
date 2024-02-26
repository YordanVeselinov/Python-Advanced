size = int(input())

matrix = []

alice_pos = []
collected_tee = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"

while collected_tee < 10:
    curr_direction = input()
    r, c = alice_pos[0] + directions[curr_direction][0], alice_pos[1] + directions[curr_direction][1]

    if not (0 <= r < size and 0 <= c < size):
        break

    alice_pos = [r, c]
    position = matrix[r][c]
    matrix[r][c] = "*"

    if position == "R":
        break

    if position.isdigit():
        collected_tee += int(position)

if collected_tee < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

# [print(*row) for row in matrix]
print(*[' '.join(row) for row in matrix], sep='\n')
