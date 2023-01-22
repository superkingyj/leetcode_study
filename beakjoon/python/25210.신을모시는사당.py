import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
prefix_1 = [0] * N
prefix_2 = [0] * N

prefix_1[0] = 1 if arr[0] == 1 else 0
for i in range(1, N):
    if arr[i] == 1: 
        prefix_1[i] = prefix_1[i-1]+1
    else: 
        prefix_1[i] = prefix_1[i-1]-1 if prefix_1[i-1] > 0 else 0

prefix_2[0] = 1 if arr[0] == 2 else 0
for i in range(1, N):
    if arr[i] == 2: 
        prefix_2[i] = prefix_2[i-1]+1
    else: 
        prefix_2[i] = prefix_2[i-1]-1 if prefix_2[i-1] > 0 else 0

max_val = 0

print(max(max(prefix_1), max(prefix_2)))


# import sys
# si = sys.stdin.readline
# n = int(si())
# a = list(map(int, si().split()))

# def solve(mapping: dict) -> int:
#     ret, cnt = 0, 0
#     for x in a:
#         cnt += mapping[x]
#         cnt = max(0, cnt)
#         ret = max(ret, cnt)
#     return ret

# print(max(solve({1:1, 2:-1}), solve({1:-1, 2:1})))