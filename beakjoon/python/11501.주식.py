import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    max_val, profit = 0, 0
    for i in range(N-1, -1, -1):
        if arr[i] >= max_val:
            max_val = arr[i]
        else:
            profit += max_val - arr[i]
        
    print(f"profit: {profit}")    