import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
points = dict()
coordi = []

for _ in range(N):
    X, R = map(int, sys.stdin.readline().split())
    if X in points: points[X].append(R)
    else: points[X] = [R]
    coordi.append(X)

coordi.sort()

def check():
    for x, _r in points.items():
        s = set()
        for r in _r:
            # 완전히 같은 원인지 확인
            if r in s: return "NO"
            else: s.add(r)

            left, right = x-r, x+r
            # 왼쪽 점에서 가장 가까운 원의 중심 찾기
            result = bisect_left(coordi, left)
            if result < len(coordi):
                left_target = coordi[result]
                
                # x와 left_p가 두점에서 만나거나 한점에서 만나는지 확인
                if left_target in points and x != left_target:
                    da, ra = left_target, max(points[left_target])
                    db, rb = x, r
                    d = abs(da-db)
                    if d == 0: continue
                    if ra+rb < d: continue
                    if d < abs(ra+rb): continue
                    return "NO"
            
            # 오른쪽 점에서 가장 가까운 원의 중심 찾기
            result = bisect_left(coordi, right)
            if result < len(coordi):
                right_target = coordi[result]
                
                # x와 right_p가 두점에서 만나거나 한점에서 만나는지 확인
                if right_target in points and x != right_target:
                    da, ra = right_target, max(points[right_target])
                    db, rb = x, r
                    d = abs(da-db)
                    if d == 0: continue
                    if ra+rb < d: continue
                    if d < abs(ra+rb): continue
                    return "NO"
    return "YES"

print(check())