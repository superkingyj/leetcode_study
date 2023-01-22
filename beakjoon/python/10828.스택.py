import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    comm = list(sys.stdin.readline().split())

    if comm[0] == "push":
        stack.append(comm[1])
    elif comm[0] == "pop":
        print(stack.pop()) if len(stack) else print(-1)
    elif comm[0] == "size":
        print(len(stack))
    elif comm[0] == "empty":
        print(0) if len(stack) else print(1)
    else: # top
        print(stack[-1]) if len(stack) else print(-1)

