import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, input().split())) for _ in range(n)]
candidates = [(i,j) for j in range(m) for i in range(n) if grid[i][j] == 0]
len_candidates = len(candidates)
virus_pos = [(i,j) for j in range(m) for i in range(n) if grid[i][j] == 2]
targets = []
visited = [[0 for _ in range(m)] for _ in range(n)]
safe_zone = 0
max_safe_zone = -sys.maxsize
q = deque()

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    global visited
    global grid

    if not in_range(x,y):
        return False
    
    if visited[x][y] or grid[x][y] != 0:
        return False
    
    return True

def push(x, y):
    global q
    global grid
    global visited 

    grid[x][y] = 2
    visited[x][y] = 1
    q.append((x,y))


# 바이러스 퍼뜨리기
def bfs():
    global visited
    global q
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    changed_list = []

    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                push(new_x, new_y)
                changed_list.append((new_x, new_y))
        
    q = deque()
    return changed_list

# safe_zone 세기
def dfs(x, y):
    global visited
    global safe_zone
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            safe_zone += 1
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)


# 어디에 벽 놓을지 고르고 벽 놓기
def backtracking(cnt, idx):
    global safe_zone
    global max_safe_zone
    global targets
    global candidates
    global len_candidates
    global q
    global virus_pos
    global visited
    changed_list = []
    
    if cnt == 3:
        # 벽 놓기
        for x, y in targets:
            grid[x][y] = 1

        # 바이러스 퍼뜨리기
        for x,y in virus_pos:
            push(x,y)
            changed_list += bfs()
        visited = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                dfs(i,j)
        visited = [[0 for _ in range(m)] for _ in range(n)]
        
        max_safe_zone = max(max_safe_zone, safe_zone)
        safe_zone = 0 

        # 벽 치우기
        for x, y in targets:
            grid[x][y] = 0
        
        for x, y in changed_list:
            if (x,y) not in virus_pos:
                grid[x][y] = 0
    
    if cnt >= 3:
        return
    
    if idx >= len_candidates:
        return
    
    # 벽이 될 target 정하기
    targets.append(candidates[idx])
    backtracking(cnt+1, idx+1)
    targets.pop()

    backtracking(cnt, idx+1)

backtracking(0, 0)
print(max_safe_zone)