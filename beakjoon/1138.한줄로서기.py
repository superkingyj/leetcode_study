import sys
from collections import deque

N = int(sys.stdin.readline())
arr = []
for idx, num in enumerate(list(map(int, sys.stdin.readline().split()))):
    arr.append((num, idx+1))
arr.sort(key = lambda x:(x[0], x[1]))

def check(idx, num):
    cnt = 0
    while idx >= 0:
        if q[idx] > num: cnt +=1
        idx -= 1
    return cnt

q = []
for i in range(N):
    if i == 0: 
        q.append(arr[i][1])
        continue
    
    tmp = deque()
    while True:
        if check(len(q)-1, arr[i][1]) == arr[i][0]:
            q.append(arr[i][1])
            q += tmp
            break
        else:
            tmp.appendleft(q.pop())

print(*q)