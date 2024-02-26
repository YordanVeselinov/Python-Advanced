from collections import deque

petrol_stations = deque([int(x) for x in input().split()] for _ in range(int(input())))

petrol_station_copy = petrol_stations.copy()

fuel_in_tank = 0
index = 0

while petrol_station_copy:
    curr_fuel, curr_distance = petrol_station_copy.popleft()

    fuel_in_tank += curr_fuel

    if fuel_in_tank >= curr_distance:
        fuel_in_tank -= curr_distance
    else:
        petrol_station_copy = petrol_stations.copy()
        petrol_station_copy.rotate(-1)
        index += 1
        fuel_in_tank = 0

print(index)
