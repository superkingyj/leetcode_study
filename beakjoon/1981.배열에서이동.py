import sys
from collections import deque

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
visited = [[False] * N for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, low, high):
    if not in_range(x,y): return False
    if visited[x][y]: return False
    if grid[x][y] < low or high < grid[x][y]: return False
    else: return True

def bfs(low, high):
    flag = False

    if not can_go(0, 0, low, high):
        return flag

    q = deque()
    visited[0][0] = True
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        if x == N-1 and y == N-1: 
            flag = True
            break

        for i in range(4):
            new_x, new_y = x+dx[i], y+dy[i]
            if can_go(new_x, new_y, low, high):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
    
    return flag

def binary_search():
    global visited
    
    nums = set()
    for i in range(N):
        for j in range(N):
            nums.add(grid[i][j])

    nums = list(nums)
    nums.sort()
    
    result = sys.maxsize
    left, right = 0, 0
    while left < len(nums):
        if bfs(nums[left], nums[right]):
            result = min(result, nums[right] - nums[left])
            left += 1
        elif right < len(nums)-1: 
            right += 1
        else:
            break
        
        visited = [[False] * N for _ in range(N)]

    return result

print(binary_search())

