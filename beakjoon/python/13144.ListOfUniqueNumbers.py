import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
check = set()
left, right = 0, 0

while right < N:
    num = arr[right]
    if num in check:
        while True:
            _num = arr[left]
            if _num not in check: break
            check.remove(_num)
            left += 1
            result += right - left
    else:
        check.add(num)
        result += right - left + 1
        right += 1

print(result)
