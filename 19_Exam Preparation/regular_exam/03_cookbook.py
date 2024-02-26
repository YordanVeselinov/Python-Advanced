def cookbook(*args):

    my_cook_book = {}
    result = ""

    for recipe, cuisine, ingredients in args:
        if cuisine not in my_cook_book:
            my_cook_book[cuisine] = {}
        my_cook_book[cuisine][recipe] = ingredients

    for cuisine, recipe_ingredients in sorted(my_cook_book.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{cuisine} cuisine contains {len(recipe_ingredients)} recipes:\n"
        for recipe, ingredients in sorted(recipe_ingredients.items(), key=lambda x: x[0], reverse=False):
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"


    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))