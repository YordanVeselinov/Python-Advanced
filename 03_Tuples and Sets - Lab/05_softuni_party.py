
tickets = set()

for _ in range(int(input())):
    reservation_numbers = input()
    tickets.add(reservation_numbers)

while True:
    came_guests = input()

    if came_guests == "END":
        break
    tickets.discard(came_guests)

print(len(tickets))

for guests_not_come in sorted(tickets):
    print(guests_not_come)
