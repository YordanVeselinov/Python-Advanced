parentheses = []
expression = input()
index = 0
for index in range(len(expression)):
    if expression[index] == "(":
        parentheses.append(index)
    if expression[index] == ")":
        start_index = parentheses.pop()
        print(expression[start_index:index+1])