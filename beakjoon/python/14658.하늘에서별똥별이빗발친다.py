import sys

N, M, L, K = map(int, sys.stdin.readline().split())
pos_x, pos_y, result = [], [], -1

def count_stars(x,y):
    cnt = 0
    for i in range(K):
        if x <= pos_x[i] <= x+L and y <= pos_y[i] <= y+L: cnt += 1

    return cnt

for i in range(K):
    x,y = map(int, sys.stdin.readline().split())
    pos_x.append(x)
    pos_y.append(y)

for x in pos_x:
    for y in pos_y:
        cnt = count_stars(x, y)
        result = max(result, cnt)
    
print(K-result)