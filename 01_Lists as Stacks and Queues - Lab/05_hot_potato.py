from collections import deque

names = deque(input().split())
number_of_tosses = int(input())
while names:
    if len(names) == 1:
        break
    names.rotate(-(number_of_tosses - 1))
    removed_name = names.popleft()
    print(f"Removed {removed_name}")
print(f"Last is",*names)