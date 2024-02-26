from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
pairs = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

all_colors = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            all_colors.append(color)
            break
    else:
        for current_color in (first_word[:-1], second_word[:-1]):
            if current_color:
                words.insert(len(words) // 2, current_color)

for color in set(pairs.keys()).intersection(all_colors):
    if not pairs[color].issubset(all_colors):
        all_colors.remove(color)

print(all_colors)