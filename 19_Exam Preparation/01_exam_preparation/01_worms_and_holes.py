from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

matches = 0
maximum_worms = len(worms)
worms_fit = 0

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_hole == current_worm:
        worms_fit += 1
        matches += 1
        continue

    if current_worm - 3 <= 0:
        continue
    worms.append(current_worm - 3)

print(f"Matches: {matches}" if matches else f'There are no matches.')

# if maximum_worms == worms_fit:
#     print(f"Every worm found a suitable hole!")
# else:
#     # if worms:
#     print(f"Worms left: {', '.join(str(x) for x in worms) if worms else 'none'}")
#     # else:
#     #     print("Worms left: none")

print(f"Every worm found a suitable hole!" if maximum_worms == worms_fit else f"Worms left: {', '.join(str(x) for x in worms) if worms else 'none'}")
print(f"Holes left: {', '.join([str(y) for y in holes])}" if holes else f"Holes left: none")
