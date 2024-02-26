size = int(input())

matrix = [list(input()) for _ in range(size)]

removed_knights = 0

directions = (
    (-2, -1), # up 2, left 1
    (-2, 1),  # up 2, right 1
    (-1, 2),  # up 1, right 2
    (1, 2),   # down 1, right 2
    (2, 1),   # down 2, right 1
    (2, -1),  # down 2 , left 1
    (1, -2),  # up 1, left 2
    (-1, -2), # down 1, right 2
)

while True:
    knight_pos_with_max = []
    max_attacks = 0

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0
                for direction in directions:
                    row_pos = row + direction[0]
                    col_pos = col + direction[1]

                    if 0 <= row_pos < size and 0 <= col_pos < size:
                        if matrix[row_pos][col_pos] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_pos_with_max = [row, col]
    if knight_pos_with_max:
        matrix[knight_pos_with_max[0]][knight_pos_with_max[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)