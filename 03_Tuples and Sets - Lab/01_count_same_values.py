numbers = tuple([float(x) for x in input().split()])
set_of_number = set(numbers)

same_numbers = {}

for num in numbers:
    if num not in same_numbers:
        same_numbers[num] = numbers.count(num)

for number, occ in same_numbers.items():
    print(f"{number:.1f} - {occ} times")