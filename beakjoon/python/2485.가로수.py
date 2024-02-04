import sys
from math import gcd

N = int(sys.stdin.readline())
prev_pos = int(sys.stdin.readline())
arr = []

for _ in range(N-1):
    num = int(sys.stdin.readline())
    arr.append(num-prev_pos)
    prev_pos = num
    
    
gcd_num = arr[0]
for i in range(N-1):
    gcd_num = gcd(gcd_num, arr[i])
    

cnt = 0
for num in arr:
    cnt += num // gcd_num-1

print(cnt)