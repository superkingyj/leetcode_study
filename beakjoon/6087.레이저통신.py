import sys
import heapq

W, H = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().rstrip() for _ in range(H)]
visited = [[False] * W for _ in range(H)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
s_x, s_y, e_x, e_y = -1, -1, -1, -1
result = sys.maxsize

def init():
    global s_x, s_y, e_x, e_y
    pos = []
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "C":
                pos.append(i)
                pos.append(j)
            if len(pos) == 4: break
        if len(pos) == 4: break
    
    s_x, s_y, e_x, e_y = pos

def in_range(x,y):
    return 0 <= x < H and 0 <= y < W

def can_go(x,y):
    if not in_range(x, y): return False
    if visited[x][y]: return False
    if grid[x][y] == "*": return False
    else: return True

def dijkstra():
    global result

    # cnt, dist, x, y, z
    q = [(0, 0, s_x, s_y, -1)]
    while q:
        cnt, dist, x, y, z = heapq.heappop(q)
        
        if x == e_x and y == e_y: 
            result = cnt
            break

        visited[x][y] = True
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y):
                if z != -1 and z != i:
                    heapq.heappush(q, (cnt+1, dist+1, new_x, new_y, i))
                else: 
                    heapq.heappush(q, (cnt, dist+1, new_x, new_y, i))     
                
init()        
dijkstra()
print(result)
