from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
q = deque()
q.append(N)
visited = [-1] * 100001
visited[N] = 0

while q:
    pos = q.popleft()
    if pos == K:
        print(visited[pos])
        break
    
    if 0 <= pos * 2 < 100001 and visited[pos*2] == -1:
        visited[pos*2] = visited[pos]
        q.append(pos*2)
    if 0 <= pos-1 < 100001 and visited[pos-1] == -1:
        visited[pos-1] = visited[pos]+1
        q.append(pos-1)
    if 0 <= pos+1 < 100001 and visited[pos+1] == -1:
        visited[pos+1] = visited[pos]+1
        q.append(pos+1)