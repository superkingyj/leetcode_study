import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
time = sys.maxsize
q = deque()
visited = [False] * 200001

def in_range(v):
    return 0 <= v <= 2*100000

def bfs():
    global time
    visited[N] = True
    q.append((N, 0))
    
    while q:
        v, t = q.popleft()

        if v == K:
            time = t
            break

        for i in range(3):
            if i == 0: new_v = v+1
            elif i == 1: new_v = v-1
            else: new_v = 2*v
            if in_range(new_v) and not visited[new_v]: 
                visited[new_v] = True
                q.append((new_v, t+1))

bfs()
print(time)