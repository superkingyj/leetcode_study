import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N))
arr.sort(key = lambda x:(-x[1], -x[2], -x[3]))

print(arr)
g, s, c = 0, 0, 0
grade = 1
cnt = 1
for i in range(N):
    if i == 0:
        g, s, c = arr[i][1], arr[i][2], arr[i][3]
    else:
        _g, _s, _c = arr[i][1], arr[i][2], arr[i][3]
        if g != _g or s != _s or c != _c:
            grade += cnt
            cnt = 1
            g, s, c = _g, _s, _c
        else:
            cnt += 1
    if arr[i][0] == K:
        print(grade)
        break