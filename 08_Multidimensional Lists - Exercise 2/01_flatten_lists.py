empty_string = input().split("|")

matrix = [x.split() for x in empty_string]

for current in matrix[::-1]:
    print(*current, end=" ") if current else None