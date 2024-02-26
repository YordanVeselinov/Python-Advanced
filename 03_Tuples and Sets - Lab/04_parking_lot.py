
parking = set()

for _ in range(int(input())):
    command, reg_plate = input().split(", ")
    if command == "IN":
        parking.add(reg_plate)
    else:
        parking.discard(reg_plate)

if parking:
    print(*parking, sep="\n")
else:
    print(f"Parking Lot is Empty")