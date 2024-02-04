# import sys

# N, K = map(int, sys.stdin.readline().split())
# coins = [int(sys.stdin.readline()) for _ in range(N)]

# result = 0

# for coin in coins[::-1]:
#     if coin > K: continue
#     result += K // coin
#     K %= coin

# print(result)

import sys

N, K = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))
result = 0

for coin in coins[::-1]:
    if coin > K: continue
    result += K // coin
    K %= coin

print(result)