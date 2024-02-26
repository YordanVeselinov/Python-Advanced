from collections import deque

green_light_dur = int(input())
free_window_dur = int(input())


current_green = 0
current_free = 0

cars_passed = 0

cars_in_queue = deque()

command = input()

while command != "END":

    if command != "green":
        car = command
        cars_in_queue.append(car)
    else:
        current_green = green_light_dur
        current_free = free_window_dur
        while cars_in_queue:
            car = cars_in_queue.popleft()
            if current_free == 0 or current_green == 0:
                break





    command = input()