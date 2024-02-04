import sys
import math

ax, ay, bx, by, cx, cy = map(int, sys.stdin.readline().split())

def check():
    return (bx-ax) * (cy-ay) == (cx-ax) * (by-ay)

def get_dist(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return math.sqrt((x * x) + (y * y))

if check():
    print(-1)
else:
    dists = [get_dist(ax, ay, bx, by), get_dist(ax, ay, cx, cy), get_dist(bx, by, cx, cy)]
    print((max(dists)-min(dists))*2)
    

"""
평행사변형 조건
1. 두 쌍의 대변의 길이가 각각 같다
2. 두 쌍의 대각의 크기가 각각 같다
3. 두 대각선은 서로 다른 대각선을 이등분한다.

"""