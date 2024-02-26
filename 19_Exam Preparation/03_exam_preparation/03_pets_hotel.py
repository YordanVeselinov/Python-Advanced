def accommodate_new_pets(available_capacity, maximum_weight, *args):
    animal_types = {}
    are_all_accommodated = True

    for animal, weight in args:
        if available_capacity == 0:
            are_all_accommodated = False
            break

        if weight <= maximum_weight:
            available_capacity -= 1
            if animal not in animal_types:
                animal_types[animal] = 0
            animal_types[animal] += 1

    result = ""

    if are_all_accommodated:
        result += f"All pets are accommodated! Available capacity: {available_capacity}.\n"
    else:
        result += "You did not manage to accommodate all pets!\n"

    result += f"Accommodated pets:\n"

    for animal_type, counter in sorted(animal_types.items()):
        result += f"{animal_type}: {counter}\n"

    return result[:-1]


