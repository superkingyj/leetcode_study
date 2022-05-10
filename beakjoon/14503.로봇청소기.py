import sys
n,m = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서
flag = False
count = 0

def can_go(x,y):
    return grid[x][y] == 0

while True:
    if flag:
        break
    
    # 현재 위치 청소
    grid[r][c] = "#"

    # 현재의 왼쪽 방향
    new_d = (d + 3) % 4 
    next_r, next_c = r+dxs[new_d], c+dys[new_d]
    
    
    # 청소하지 않은 빈 공간이 있다면
    if can_go(next_r, next_c):
        count = 0
        # 왼쪽 방향으로 회전
        d = new_d
        # 한칸 전진
        r, c = next_r, next_c
    # 그렇지 않다면
    else:
        # 왼쪽 방향으로 회전
        d = new_d
        count += 1

    
    if count >= 4:
        back_d = (d + 2) % 4
        back_r, back_c = r+dxs[back_d], c+dys[back_d]

        if grid[back_r][back_c] == 1:
            flag = True
        else:
            r, c = back_r, back_c
            count = 0

result = 0
for i in range(n):
     for j in range(m):
        if grid[i][j] == "#":
            result += 1
print(result)