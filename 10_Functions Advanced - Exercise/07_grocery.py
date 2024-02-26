def grocery_store(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda x: ((-x[1]), -len(x[0]), (x[0])))
    formatted_string = ''
    for name, quantity in sorted_result:
        formatted_string += f"{name}: {quantity}\n"
    return formatted_string


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))