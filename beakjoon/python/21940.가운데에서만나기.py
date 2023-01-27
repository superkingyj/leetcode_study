import sys 

N, M = map(int, sys.stdin.readline().split())
dist = [[sys.maxsize] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B, T = map(int, sys.stdin.readline().split())
    dist[A][A] = 0
    dist[A][B] = min(dist[A][B], T)

K = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def floyd_warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

floyd_warshall()
min_rt = sys.maxsize
result = []

for i in range(1, N+1):
    max_rt = 0
    
    for j in arr:
        max_rt = max(max_rt, dist[i][j]+dist[j][i])
    
    if max_rt == sys.maxsize: continue
    
    if max_rt < min_rt:
        min_rt = max_rt
        result = [i]
    elif max_rt == min_rt:
        result.append(i)

result.sort()
print(*result)