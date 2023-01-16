import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)

def backtracking(cnt, arr, idx):
    if cnt == M:
        print(*arr)
        return

    for i in range(idx, N+1):
        if not visited[i]:
            visited[i] = True
            backtracking(cnt+1, arr+[i], i+1)
            visited[i] = False

backtracking(0, list(), 1)