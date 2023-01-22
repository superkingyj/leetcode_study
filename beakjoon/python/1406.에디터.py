import sys
from collections import deque

S = deque(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())

l, r = S, deque()
for _ in range(M):
    q = sys.stdin.readline().rstrip().split()

    if q[0] == "L":
        if l: r.appendleft(l.pop())
    elif q[0] == "D":
        if r: l.append(r.popleft())
    elif q[0] == "B":
        if l: l.pop()
    else: l.append(q[1])

print("".join(l+r))