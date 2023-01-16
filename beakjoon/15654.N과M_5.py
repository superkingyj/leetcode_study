import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
visited = [False] * (N+1)
lst.sort()

def backtracking(cnt, arr):
    if cnt == M: 
        print(*arr)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtracking(cnt+1, arr + [lst[i]])
            visited[i] = False

backtracking(0, list())