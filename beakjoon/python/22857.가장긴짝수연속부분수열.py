import sys

def two_pointer(arr, n, k):
    max_even_subarrray, even_subarrray, p2, cnt = 0, 0, 0, 0
    
    for i in range(n):
        p1 = i
        while True:
            if p2 >= n or cnt > k: break
            if arr[p2] % 2: cnt += 1
            else: even_subarrray += 1
            p2 += 1
            
        max_even_subarrray = max(max_even_subarrray, even_subarrray)
        
        if arr[p1] % 2: cnt -= 1
        else: even_subarrray -= 1

    return max_even_subarrray

n, k = map(int, sys.stdin.readline().split())
arr = [int(i) for i in sys.stdin.readline().split()]
print(two_pointer(arr, n, k))