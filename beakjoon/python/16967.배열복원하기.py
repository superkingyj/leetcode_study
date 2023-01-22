import sys

H, W, X, Y = map(int, sys.stdin.readline().split())
arr_b = [list(map(int, sys.stdin.readline().split())) for _ in range(H+X)]
arr_a = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i >= X and j >= Y:
            arr_a[i][j] = arr_b[i][j] - arr_a[i-X][j-Y]
        else:
            arr_a[i][j] = arr_b[i][j]

for i in range(H):
    print(*arr_a[i])