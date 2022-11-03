import sys
from collections import Counter, defaultdict

T = int(sys.stdin.readline())
result = ""

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = [0] * 201
    counter = Counter(arr)
    grade = defaultdict(list)
    idx = 1
    
    for key, val in counter.items():
        cnt[key] = val
    
    for i in range(N):
        if cnt[arr[i]] < 6: continue
        grade[arr[i]].append(idx)
        idx += 1
    
    win_team, win_score = 0, sys.maxsize
    for key, val in grade.items():
        score = sum(val[:4])
        if score < win_score: win_team, win_score = key, score
        elif score == win_score:
            if val[-2] < grade[win_team][-2]: win_team, win_score = key, score
    
    result += str(win_team) + "\n"

print(result)