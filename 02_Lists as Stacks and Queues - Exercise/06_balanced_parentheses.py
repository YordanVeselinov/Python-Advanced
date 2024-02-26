from collections import deque

parentheses = deque(input())
opening_parentheses = deque()
closing_brackets = deque()

parentheses_copy = parentheses.copy()

for char in parentheses:
    if char in "({[": # "()"
        opening_parentheses.append(char)
    elif char in ")}]":
        closing_brackets.append(char)
        current_open = opening_parentheses.pop() if opening_parentheses else " "
        current_closed = closing_brackets.pop() if closing_brackets else ' '
        if not current_open + current_closed in "(){}[]":
            print(f"NO")
            break
else:
    print("YES")