import sys
from collections import defaultdict
from collections import deque 

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = defaultdict(list)

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            graph[i+1].append(j+1)

plan = list(map(int, sys.stdin.readline().split()))

def djikstra(s):
    q = deque()
    q.append(s)
    dist = set()
    
    while q:
        s = q.popleft()
        if s not in dist:
            dist.add(s)
            for e in graph[s]:
                q.append(e)
    
    return dist

flag = False
for i in range(len(plan)-1):
    dist = djikstra(plan[i])
    if plan[i+1] not in dist:
        flag = True
        break

if flag: print("NO")
else: print("YES")