# Solution 1
# from collections import deque
#
# expression = deque(input().split())
#
#
# index = 0
#
#
# while index < len(expression):
#
#     element = expression[index]
#
#     if element == "*":
#         for _ in range(index-1):
#             expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
#     elif element == "/":
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
#     elif element == "+":
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#     elif element == "-":
#         for _ in range(index - 1):
#             expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
#
#     if element in "/*-+":
#         del expression[1]
#         index = 1
#
#     index += 1
#
# print(int(expression[0]))

# Solution 2
from collections import deque
from functools import reduce

expression = input().split()


index = 0

func =  {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
}


while index < len(expression):

    element = expression[index]

    if element in "/*+-":
        expression[0] = func[element](index)
        [expression.pop(1) for _ in range(index)]  # pop everything including the symbol
        index = 1

    index += 1

print(int(expression[0]))
