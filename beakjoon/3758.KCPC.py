import sys
from collections import defaultdict

T = int(sys.stdin.readline())

def get_grade(score, last_time, cnt, logs, t, n):
    time = 1
    for i, j, s in logs:
        score[i][j] = max(score[i][j], s)
        cnt[i] += 1
        last_time[i] = time
        time += 1

    score_lst = []
    for key, val in score.items():
        score_lst.append((key, sum(val), cnt[key], last_time[key]))
    score_lst.sort(key = lambda x:(-x[1], x[2], x[3]))

    for i in range(n):
        if score_lst[i][0] == t: return i+1

for _ in range(T):
    n, k, t, m = map(int, sys.stdin.readline().split())
    score = dict()
    for i in range(1, n+1):
        score[i] = [0] * (k+1)
    last_time = defaultdict(int)
    cnt = defaultdict(int)
    logs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(get_grade(score, last_time, cnt, logs, t, n))