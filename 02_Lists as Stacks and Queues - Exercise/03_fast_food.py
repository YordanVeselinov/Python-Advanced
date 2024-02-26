from collections import deque

quantity_of_food = int(input())
orders = deque(int(x) for x in input().split())

biggest_order = max(orders)

while orders:
    order = orders.popleft()
    if order <= quantity_of_food:
        quantity_of_food -= order
    else:
        orders.appendleft(order)
        break
print(biggest_order)

if orders:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
else:
    print(f"Orders complete")
