import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
dna_list = list(sys.stdin.readline().rstrip() for _ in range(N))
result_dna = ""
sum_val = 0

for j in range(M):
    cnt = defaultdict(int)
    for i in range(N):
        cnt[dna_list[i][j]] += 1
    cnt_list = list(cnt.items())
    cnt_list.sort(key = lambda x:(-x[1], x[0]))
    result_dna += cnt_list[0][0]
    sum_val += sum(cnt_list[i][1] for i in range(1, len(cnt_list)))
    
print(result_dna)
print(sum_val)
    