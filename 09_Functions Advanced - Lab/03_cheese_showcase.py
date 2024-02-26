def sorting_cheeses(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), (x[0])))
    formatted_string = ''

    for name, value in result:
        formatted_string += name + '\n'
        for current in sorted(value,reverse=True):
            formatted_string += str(current) + '\n'
    return formatted_string



print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
