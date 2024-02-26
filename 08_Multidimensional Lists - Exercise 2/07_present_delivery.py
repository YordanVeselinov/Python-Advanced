def eat_cookie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if matrix[r][c].isalpha():
            if matrix[r][c] == 'V':
                nice_kids += 1

            matrix[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

matrix = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    line = input().split()

    matrix.append(line)

    if 'S' in line:
        santa_pos = [row, line.index('S')]
        matrix[row][santa_pos[1]] = '-'
    total_nice_kids += line.count('V')

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]

    house = matrix[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        nice_kids_visited += 1
        presents -= 1
    elif house == 'C':
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    matrix[santa_pos[0]][santa_pos[1]] = '-'

    if not presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

matrix[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and nice_kids_visited < total_nice_kids:
    print('Santa ran out of presents!')

print(*[' '.join(line) for line in matrix], sep='\n')

if total_nice_kids == nice_kids_visited:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')