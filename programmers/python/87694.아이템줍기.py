from collections import deque
from pprint import pprint
grid, visited = [], []
N, M = 0, 0 

def in_range(x, y):
    return 0 <= x < N+2 and 0 <= y < M+2

def bfs(start_x, start_y, end_x, end_y):
    global grid
    
    q = deque()
    q.append((start_x, start_y, 0))
    grid[start_x][start_y] = "#"
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    answer = 0
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == end_x and y == end_y:
            answer = cnt//2
            break
        
        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if grid[new_x][new_y] == "*":
                grid[new_x][new_y] = "#"
                q.append((new_x, new_y, cnt+1))
        
    return answer
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    global N, M, grid, visited
    answer = 0
    
    for x1, y1, x2, y2 in rectangle:
        N = max(N, x2*2)
        M = max(M, y2*2)
        
    grid = [["."] * (M+2) for _ in range(N+2)]
    
    # 사각형 내부 채우기
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1*2, (x2*2)+1):
            for y in range(y1*2, (y2*2)+1):
                grid[x][y] = "#"
    
    dx, dy = [-1, -1,-1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    
    # 사각형 외곽 찾기
    for x in range(N+2):
        for y in range(M+2):
            if grid[x][y] != "#": continue
            for i in range(8):
                new_x, new_y = x+dx[i], y+dy[i]
                if in_range(new_x, new_y) and grid[new_x][new_y] == ".":
                    grid[x][y] = "*"
                    break
    
    for i in range(N+2):
        print(grid[i])
        print()
    answer = bfs(characterX*2, characterY*2, itemX*2, itemY*2)
    
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1,1,5,7]], 1, 1, 4, 7))
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))
