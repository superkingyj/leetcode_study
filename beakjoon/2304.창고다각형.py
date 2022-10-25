import sys

N = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr.sort()
left, right = 0, N-1
l_cur, r_cur = arr[0][0], arr[-1][0]+1
l_max, r_max = arr[0][1], arr[-1][1]
result = 0

while left <= right:
    if l_max < arr[left][1]:
        result += l_max * (arr[left][0] - l_cur)
        l_cur = arr[left][0]
        l_max = arr[left][1]
    if r_max < arr[right][1]:
        result += r_max * (r_cur - (arr[right][0]+1))
        r_cur = arr[right][0]+1
        r_max = arr[right][1]

    if l_max <= r_max: left += 1
    else: right -= 1

result += r_max * (r_cur - l_cur)
print(result)
