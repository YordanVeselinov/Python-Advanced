import datetime
from collections import deque

robots_info = [x for x in input().split(";")]

time = datetime.datetime.strptime(input(), "%H:%M:%S")

robots = {}


for info in robots_info:
    robots_name, work_time = info.split("-")
    if robots_name not in robots.items():
        robots[robots_name] = [int(work_time), 0]

tasks = deque()
command = input()

while command != "End":
    tasks.append(command)
    command = input()

while tasks:
    time += datetime.timedelta(0,1)
    current_task = tasks.popleft()

    free_robots = []
    for robot, work_time_info in robots.items():
        if work_time_info[1] != 0:
            robots[robot][1] -= 1

        if work_time_info[1] == 0:
            free_robots.append([robot, work_time_info])

    if not free_robots:
        tasks.append(current_task)
        continue

    free_robot, data = free_robots[0]
    robots[free_robot][1] = data[0]

    print(f"{free_robot} - {current_task} [{time.strftime('%H:%M:%S')}]")


