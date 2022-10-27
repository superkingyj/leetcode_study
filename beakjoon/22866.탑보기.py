import sys
from collections import deque

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
left = deque()
stack = deque()

for idx, num in enumerate(arr):
    if not stack:
        stack.append(idx)
        left.append(-1)
        continue
    
    while True:
        if not stack: break
        _idx = stack[-1]
        _val = arr[_idx]
        if _val > num: break
        stack.pop()
    
    left.append(stack[-1]+1 if stack else -1)
    stack.append(idx)

stack = deque()
right = deque()
for idx, num in enumerate(arr[::-1]):
    idx = N-(idx+1)
    if not stack:
        stack.append(idx)
        right.append(-1)
        continue
    
    while True:
        if not stack: break
        _idx = stack[-1]
        _val = arr[_idx]
        if _val > num: break
        stack.pop()
    
    right.appendleft(stack[-1]+1 if stack else -1)
    stack.append(idx)

l_total = [0] * N
r_total = [0] * N
total = [0] * N
for i in range(N):
    l_idx, r_idx = i, (N-i)-1
    if left[l_idx] != -1: l_total[l_idx] += 1+l_total[left[l_idx]-1]
    if right[r_idx] != -1: r_total[r_idx] += 1+r_total[right[r_idx]-1]

for i in range(N):
    total[i] = l_total[i] + r_total[i]

for i in range(N):
    if left[i] < 0 and right[i] < 0:
        print(0)
        continue
    if left[i] < 0:
        target = right[i]
    elif not right[i]:
        target = left[i]
    else: 
        if abs(i+1 - left[i]) <= abs(i+1 - right[i]):
            target = left[i]
        else:
            target = right[i]
    print(total[i], target)