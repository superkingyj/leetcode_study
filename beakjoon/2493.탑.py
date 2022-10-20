import sys

N  = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
result = [0] * N

for i in range(N):
    while stack:
        idx, val = stack.pop()
        if val > arr[i]:
            result[i] = idx
            stack.append((idx, val))
            break

    stack.append((i+1, arr[i]))
print(*stack)