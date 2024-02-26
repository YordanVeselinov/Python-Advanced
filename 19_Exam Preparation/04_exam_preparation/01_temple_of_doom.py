from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()

    searched_challenge = tool * substance

    if searched_challenge in challenges:
        challenges.remove(searched_challenge)
    else:
        tools.append(tool + 1)
        substances.append(substance - 1) if substance - 1 > 0 else None

    if not challenges:
        print(f"Harry found an ostracon, which is dated to the 6th century BCE.")
        break
else:
    print(f"Harry is lost in the temple. Oblivion awaits him.")

print(f"Tools: {', '.join(str(x) for x in tools)}") if tools else None
print(f"Substances: {', '.join(str(x) for x in substances)}") if substances else None
print(f"Challenges: {', '.join(str(x) for x in challenges)}") if challenges else None
