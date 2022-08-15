import sys

s = int(sys.stdin.readline())
n, num = 0, 0

for i in range(1,s):
    n += 1
    num += i
    
    if num > s: break

print(n-1)