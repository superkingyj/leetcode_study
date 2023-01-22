import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().split())
total = A+B+C
visited = [[False] * total for _ in range(total)]

def bfs():
    flag = False
    q = deque()
    visited[A][B] = True
    q.append((A, B))

    while q:
        x, y = q.popleft()
        z = total-(x+y)

        if x == y == z:
            flag = True
            break
        
        for a, b in (x,y), (x, z), (y, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else: 
                continue

            c = total-(a+b)
            new_x, new_y = min(a,b,c), max(a,b,c)
            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

    return flag

if total % 3: print(0)
else:
    if bfs(): print(1)
    else: print(0)




