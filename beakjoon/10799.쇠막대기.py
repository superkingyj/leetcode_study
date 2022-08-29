import sys
from collections import deque

input = deque(sys.stdin.readline())
stack = []
result = 0

while len(input) > 0:

    char = input.popleft()
    if char == "(" and input[0] == ")":
        result += len(stack)
        input.popleft()
    elif char == "(":
        stack.append("(")
    elif char == ")":
        result += 1
        stack.pop()

print(result)