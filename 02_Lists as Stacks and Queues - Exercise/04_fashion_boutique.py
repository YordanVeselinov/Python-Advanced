from collections import deque

clothes = deque(int(x)for x in input().split())
rack_capacity = int(input())
racks_needed = 1

current_rack = rack_capacity

while clothes:
    current_clothe = clothes.pop()
    if current_clothe <= current_rack:
        current_rack -= current_clothe
    else:
        current_rack = rack_capacity - current_clothe
        racks_needed += 1

print(racks_needed)