from string import punctuation


with open("resources/ex_02/text_02.txt", "r") as file:
    text = file.readlines()

with open("resources/ex_02/output_02.txt", "a") as output:

    for row in range(len(text)):
        letters, current_punctuation = 0, 0

        for char in text[row]:
            if char.isalpha():
                letters += 1
            elif char in punctuation:
                current_punctuation += 1

        output.write(f"Line {row + 1}: {text[row][:-1]} ({letters})({current_punctuation})\n")