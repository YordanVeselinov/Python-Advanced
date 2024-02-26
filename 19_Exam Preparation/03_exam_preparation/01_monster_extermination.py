from collections import deque

armor_of_monsters = deque([int(x) for x in input().split(",")])
soldier_striking_power = [int(x) for x in input().split(",")]

monsters_killed = 0

while armor_of_monsters and soldier_striking_power:
    curr_armor = armor_of_monsters.popleft()
    curr_strike = soldier_striking_power.pop()

    if curr_strike >= curr_armor:
        monsters_killed += 1
        remaining_impact = curr_strike - curr_armor

        if soldier_striking_power and remaining_impact > 0:
            soldier_striking_power[-1] += remaining_impact

        elif not soldier_striking_power and remaining_impact > 0:
            soldier_striking_power.append(remaining_impact)

    elif curr_strike < curr_armor:
        remaining_impact = abs(curr_strike - curr_armor)
        armor_of_monsters.append(remaining_impact)

if not armor_of_monsters:
    print(f"All monsters have been killed!")
if not soldier_striking_power:
    print(f"The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
