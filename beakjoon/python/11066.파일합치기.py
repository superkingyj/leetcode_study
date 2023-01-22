import sys

T = int(sys.stdin.readline())

def dynamic_programming(N, arr):
    dp = [0] * (N+1)


for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(dynamic_programming(N, arr))