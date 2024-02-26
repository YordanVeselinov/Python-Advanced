from collections import deque

fuel_quantity = [int(x) for x in input().split()]
consumption_index = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])
top = len(fuel_needed)

counter = 0
altitudes = []

while fuel_needed and fuel_quantity and fuel_needed:
    current_fuel = fuel_quantity.pop()
    current_consumption = consumption_index.popleft()
    current_needed_fuel = fuel_needed.popleft()

    current_result = current_fuel - current_consumption

    if current_result >= current_needed_fuel:
        counter += 1
        altitudes.append(f"Altitude {counter}")
        print(f"John has reached: Altitude {counter}")
    else:
        print(f'John did not reach: Altitude {counter + 1}')
        break




if counter == top:
    print(f"John has reached all the altitudes and managed to reach the top!")
elif counter > 0:
    print(f'John failed to reach the top.')
    print(f'Reached altitudes: {", ".join(altitudes)}')
else:
    print(f"John failed to reach the top.")
    print("John didn't reach any altitude.")