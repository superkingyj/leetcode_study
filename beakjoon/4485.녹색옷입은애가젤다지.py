import sys
import heapq
from collections import defaultdict

cnt = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0: break

    grid = [list(map(int, input().split())) for _ in range(N)]
    graph = defaultdict(list)

    # 그래프 만들기
    for i in range(N):
        for j in range(N):
            if 0 <= i+1 < N: graph[(i,j)].append((grid[i+1][j], i+1,j))
            if 0 <= j+1 < N: graph[(i,j)].append((grid[i][j+1], i,j+1))
            if 0 <= i-1 < N: graph[(i,j)].append((grid[i-1][j], i-1,j))
            if 0 <= j-1 < N: graph[(i,j)].append((grid[i][j-1], i,j-1)) 

    
    q = [(grid[0][0], 0, 0)] 
    dist = defaultdict(int)

    # 다익스트라 
    while q:
        lose, x, y = heapq.heappop(q)
        if (x,y) not in dist:
            dist[(x,y)] = lose
            for lose_, x, y in graph[(x,y)]:
                alt = lose + lose_
                heapq.heappush(q, (alt, x, y))
    
    print(f"Problem {cnt}: {dist[(N-1, N-1)]}")