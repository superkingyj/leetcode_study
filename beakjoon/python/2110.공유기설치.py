import sys

N, C = map(int, sys.stdin.readline().split())
arr = list(int(sys.stdin.readline()) for _ in range(N))
arr.sort()

def paramatric_search(left, right):
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        cur = arr[0]
        cnt = 1

        for i in range(1, N):
            if arr[i] >= cur + mid:
                cnt += 1
                cur = arr[i]
        
        if cnt >= C:
            left = mid+1
            answer = mid
        else:
            right = mid-1
    
    return answer

left, right = 1, arr[-1]-arr[0] 
print(paramatric_search(left, right))
