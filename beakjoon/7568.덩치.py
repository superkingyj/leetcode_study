import sys

N = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0]*N

for i in range(N):
    w, h = arr[i][0], arr[i][1]
    grade = 1
    left, right = i-1, i+1
    
    while left >= 0:
        _w, _h = arr[left][0], arr[left][1]
        if _w > w and _h > h: grade += 1
        left -= 1
    
    while right < N:
        _w, _h = arr[right][0], arr[right][1]
        if _w > w and _h > h: grade += 1
        right += 1
    
    result[i] = grade

print(*result)
