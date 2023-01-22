import sys
from itertools import combinations

# 풀이 1
# N = int(sys.stdin.readline())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# result = float('inf')
# members = [i for i in range(N)]
# 
# for t1_mem in list(combinations(members, N//2)):
#     t1, t2 = 0, 0
#     t2_mem = list(set(members) - set(t1_mem))  
#     for i, j in list(combinations(t1_mem, 2)):
#         t1 += arr[i][j]
#         t1 += arr[j][i]
#     for i, j in list(combinations(t2_mem, 2)):
#         t2 += arr[i][j]
#         t2 += arr[j][i]
#     result = min(result, abs(t1-t2))
# print(result)


N = int(sys.stdin.readline())
N //= 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allstat = sum(newstat) // 2

mins = 65535
for l in combinations(newstat[:-1], N):
    mins = min(mins, abs(allstat - sum(l)))
print(mins)