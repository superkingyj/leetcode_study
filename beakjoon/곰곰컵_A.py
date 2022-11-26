import sys

N = int(sys.stdin.readline())
cnt = 0 

for _ in range(N):
    date = int(sys.stdin.readline().rstrip()[2:])
    if date <= 90: cnt += 1

print(cnt)
