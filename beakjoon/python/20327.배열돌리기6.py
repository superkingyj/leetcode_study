import sys

N, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(pow(2, N))]
query = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(R))

# 각 부분배열 상하 반전
def calc_1(L):
    if L == 0: return
    for i in range(0, pow(2, N), pow(2, L)):
        for j in range(0, pow(2, N), pow(2, L)):
            cnt = pow(2, L)-1
            for k in range(pow(2, L)//2):
                for l in range(pow(2, L)):
                    arr[i+k][j+l], arr[i+k+cnt][j+l] = arr[i+k+cnt][j+l], arr[i+k][j+l]
                cnt -= 2


# 각 부분배열 좌우 반전
def calc_2(L):
    if L == 0: return
    for i in range(0, pow(2, N), pow(2, L)):
        for j in range(0, pow(2, N), pow(2, L)):
            for k in range(pow(2, L)):
                cnt = pow(2, L)-1
                for l in range(pow(2, L)//2):
                    arr[i+k][j+l], arr[i+k][j+l+cnt] = arr[i+k][j+l+cnt], arr[i+k][j+l]
                    cnt -= 2

# 각 부분배열 오른쪽 90도 회전
def calc_3(L):
    if L == 0: return
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우, 하, 좌, 상
    
    for i in range(0, pow(2, N), pow(2, L)):
        for j in range(0, pow(2, N), pow(2, L)):           
            
            s_x, s_y, cnt = i, j, 1
            for _ in range(pow(2, L)//2):
                tmp = arr[s_x][s_y]
                x, y, dir = s_x, s_y+1, 0
                while True:
                    if x == s_x+1 and y == s_y: break
                    new_x, new_y = x+dx[dir], y+dy[dir]
                    if cnt % pow(2, L) == 0:
                        dir = (dir + 1) % 4
                        continue
                    arr[x][y], tmp = tmp, arr[x][y]
                    cnt += 1
                    x, y = new_x, new_y
                
                s_x += 1
                s_y += 1
                cnt -= 1



# 각 부분배열 왼쪽 90도 회전
def calc_4(l):
    pass

# 배열 상하 반전
def calc_5(l):
    pass

# 배열 좌우 반전
def calc_6(l):
    pass

# 배열 오른쪽 90도 회전
def calc_7(l):
    pass

# 배열 왼쪽 90도 회전
def calc_8(l):
    pass

for k, l in query:
    if k == 1: calc_1(l)
    elif k == 2: calc_2(l)
    elif k == 3: calc_3(l)
    elif k == 4: calc_4(l)
    elif k == 5: calc_5(l)
    elif k == 6: calc_6(l)
    elif k == 7: calc_7(l)
    else: calc_8(l)

