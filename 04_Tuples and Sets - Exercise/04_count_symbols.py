sequence = list(input())

unique = set(sequence)

for char in sorted(unique):
    print(f"{char}: {sequence.count(char)} time/s")
