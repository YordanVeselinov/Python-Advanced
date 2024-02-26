from collections import deque

names_in_queue = deque()

water_quantity = int(input())

names = input()
while names != "Start":
    names_in_queue.append(names)

    names = input()

command = input()
while command != "End":
    command = command.split()
    if len(command) == 1:
        water_needed = int(command[0])
        if water_needed <= water_quantity:
            current_customer = names_in_queue.popleft()
            water_quantity -= water_needed
            print(f"{current_customer} got water")
        else:
            current_customer = names_in_queue.popleft()
            print(f"{current_customer} must wait")

    elif len(command) == 2:
        _, refill_watter = command
        water_quantity += int(refill_watter)
    command = input()
print(f'{water_quantity} liters left')