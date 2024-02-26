from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

crafted = []
crafted_toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic:
    material = materials.pop() if magic[0] or not materials[-1] else 0
    current_magic = magic.popleft() if material or not magic[0] else 0

    if not current_magic:
        continue

    product = material * current_magic

    if crafted_toys.get(product):
        crafted.append(crafted_toys[product])
    elif product < 0:
        materials.append(material + current_magic)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]

