first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

func = {
    "Add First": lambda x: [first_sequence.add(int(num)) for num in x],
    "Add Second": lambda x: [second_sequence.add(int(num)) for num in x],
    "Remove First": lambda x: [first_sequence.discard(int(num)) for num in x],
    "Remove Second": lambda x: [second_sequence.discard(int(num)) for num in x],
    "Check Subset": lambda x: print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
}

for _ in range(int(input())):
    command_first, command_second, *data = input().split()
    full_command = command_first + " " + command_second
    func[full_command](data)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")


