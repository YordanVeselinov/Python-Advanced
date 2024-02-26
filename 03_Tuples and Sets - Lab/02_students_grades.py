students = {}

for _ in range(int(input())):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    average = sum(grades) / len(grades)
    formatted_str = f"{' '.join([f'{x:.2f}' for x in grades])}"
    print(f"{name} -> {formatted_str} (avg: {average:.2f})")
