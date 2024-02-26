from collections import deque

ducks_collected = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

programmers_time = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

while programmers_time and number_of_tasks:
    current_programmers_time = programmers_time.popleft()
    current_task = number_of_tasks.pop()

    products = current_programmers_time * current_task

    if 0 <= products <= 60:
        ducks_collected["Darth Vader Ducky"] += 1
    elif 61 <= products <= 120:
        ducks_collected["Thor Ducky"] += 1
    elif 121 <= products <= 180:
        ducks_collected["Big Blue Rubber Ducky"] += 1
    elif 181 <= products <= 240:
        ducks_collected["Small Yellow Rubber Ducky"] += 1
    else:
        programmers_time.append(current_programmers_time)
        number_of_tasks.append(current_task - 2)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck_name, value in ducks_collected.items():
    print(f"{duck_name}: {value}")

