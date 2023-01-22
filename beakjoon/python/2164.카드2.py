import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for i in range(N):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q.popleft())