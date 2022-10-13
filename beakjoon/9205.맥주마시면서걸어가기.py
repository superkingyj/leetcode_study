import sys
from collections import deque

def can_go(idx, x, y, cvs_x, cvs_y):
    if visited[idx]: return False
    elif abs(x-cvs_x) + abs(y-cvs_y) > 1000: return False
    else: return True

def bfs(s_x, s_y):
    visited[0] = True
    q.append((s_x, s_y))

    while q:
        x, y = q.popleft()
        print(f"x:{x}, y:{y}")
        for idx, item in enumerate(cvs_list):
            cvs_x, cvs_y = item[0], item[1]
            if can_go(idx, x, y, cvs_x, cvs_y):
                visited[idx] = True
                q.append((cvs_x, cvs_y))

N = int(sys.stdin.readline())
for _ in range(N):
    cvs_cnt = int(sys.stdin.readline())
    s_x, s_y = map(int, sys.stdin.readline().split())
    cvs_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(cvs_cnt)]
    e_x, e_y = map(int, sys.stdin.readline().split())
    cvs_list = [(s_x, s_y)] + cvs_list
    cvs_list.append((e_x, e_y))

    q = deque()
    visited = [False] * (cvs_cnt+2)
    
    print(cvs_list)
    bfs(s_x, s_y)
    print(visited)
    print("happy") if visited[-1] else print("sad")


"""
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
"""