
odd_sums = set()
even_sums = set()

for divider in range(1, int(input()) + 1):
    current_sum = sum([ord(x) for x in input()]) // divider
    if current_sum % 2 == 0:
        even_sums.add(current_sum)
    else:
        odd_sums.add(current_sum)

if sum(odd_sums) == sum(even_sums):
    print(*even_sums.union(odd_sums), sep=", ")
elif sum(odd_sums) > sum(even_sums):
    print(*odd_sums.difference(even_sums), sep=", ")
else:
    print(*even_sums.symmetric_difference(odd_sums), sep=", ")