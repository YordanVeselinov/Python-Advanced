from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    current_milk = cups_of_milk.popleft()

    if current_milk == chocolate:
        milkshakes += 1
    elif current_milk <= 0:
        chocolates.append(chocolate)
    elif chocolate <= 0:
        cups_of_milk.appendleft(current_milk)
    else:
        cups_of_milk.append(current_milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print('Chocolate: empty')

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")