def team_lineup(*args):
    contries = {}
    for name, country in args:
        contries.setdefault(country, []).append(name)

    result = sorted(contries.items(), key=lambda x: (-len(x[1]), x[0]))

    formatted_result = ""

    for country, players in result:
        formatted_result += country + ":\n"
        for player in players:
            formatted_result += f"  -{player}\n"

    return formatted_result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
