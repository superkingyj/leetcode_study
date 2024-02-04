import sys
import bisect 

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# DP[i] = arr[i]를 마지막 원소로 가지고 있을 때 가장 긴 증가하는 부분 수열
DP = [arr[0]]

for i in range(N):
    # 만약 arr[i]기 DP[-1]보다 크다면 DP에 추가
    if arr[i] > DP[-1]:
        DP.append(arr[i])
    # 더 작을 경우 맞는 위치를 찾아서 변경
    else:
        idx = bisect.bisect_left(DP, arr[i])
        DP[idx] = arr[i]

# print(DP)
print(N-len(DP))