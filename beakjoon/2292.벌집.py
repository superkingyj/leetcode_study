import sys

N = int(sys.stdin.readline())

left, right, tmp, cnt = 1, 2, 6, 1
while True: 
    if left <= N < right: break
    else: 
        left, right = right, right+tmp
        tmp += 6
        cnt += 1

print(cnt)