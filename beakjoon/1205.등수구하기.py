import sys

def binary_search():
    left, right = 0, N+1
    idx = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > M:
            left = mid+1
            idx = left
        else:
            right = mid-1
    return idx

N, M, P, = map(int, sys.stdin.readline().split())
if N != 0: arr = list(map(int, sys.stdin.readline().split()))
else: arr = []

if not arr:
    print(1)
elif len(arr) < P or (arr[-1] < M):
    arr = [sys.maxsize] + arr + [-sys.maxsize]
    idx = binary_search()
    arr.insert(idx, M)
    grade, tmp = 1, 1

    for i in range(1, N+1):
        if arr[i] == M and arr[i] > arr[i+1]: 
            break
        if arr[i] == arr[i+1]:
            tmp += 1
        else:
            grade += tmp
            tmp = 1

    print(grade if grade <= P else -1)
else: print(-1)