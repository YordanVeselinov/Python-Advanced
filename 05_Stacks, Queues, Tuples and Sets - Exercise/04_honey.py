from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

collected_nectar = 0

while working_bees and nectar:
    bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < bee:
        working_bees.appendleft(bee)
    else:
        symbol = symbols.popleft()
        result = 0
        if symbol == "*":
            result = abs(bee * current_nectar)
        elif symbol == "-":
            result = abs(bee - current_nectar)
        elif symbol == "+":
            result = abs(bee + current_nectar)
        elif symbol == "/":
            if current_nectar == 0:
                continue
            result = abs(bee / current_nectar)
        collected_nectar += result

print(f"Total honey made: {collected_nectar}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
