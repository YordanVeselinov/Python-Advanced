
longest_intersection = set()

for _ in range(int(input())):
    first_info, second_info = input().split("-")
    first_start, first_stop = first_info.split(",")
    second_start, second_stop = second_info.split(",")
    first_set = set(range(int(first_start), int(first_stop) + 1))
    second_set = set(range(int(second_start), int(second_stop) + 1))
    current_intersection = first_set.intersection(second_set)
    if len(longest_intersection) <= len(current_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in sorted(longest_intersection)])}] with length {len(longest_intersection)}")