from collections import deque

numbers = deque()

map_func = {
    "1": lambda x: numbers.append(int(x[1])),
    "2": lambda x: numbers.pop() if numbers else None,
    "3": lambda x: print(max(numbers)) if numbers else None,
    "4": lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    command = input().split()
    map_func[command[0]](command)

numbers.reverse()

print(*numbers, sep=", ")