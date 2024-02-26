from collections import deque

money = [int(x) for x in input().split()]
prices_of_food = deque([int(x) for x in input().split()])
food_counter = 0

while money and prices_of_food:
    current_change = money.pop()
    current_price = prices_of_food.popleft()

    if current_price == current_change:
        food_counter += 1
    elif current_change > current_price:
        food_counter += 1
        difference = current_change - current_price
        if money:
            money[-1] += difference
        else:
            money.append(difference)
    elif current_change < current_price:
        continue

if food_counter >= 4:
    print(f"Gluttony of the day! Henry ate {food_counter} foods.")
elif 0 < food_counter < 4:
    if food_counter == 1:
        print(f"Henry ate: {food_counter} food.")
    else:
        print(f"Henry ate: {food_counter} foods.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")
