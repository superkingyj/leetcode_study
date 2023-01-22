from collections import deque
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    target_p = sys.stdin.readline().replace('\n','')
    n = int(sys.stdin.readline())
    if n:
        target_nums = deque(map(int, sys.stdin.readline().lstrip("[").rstrip("]\n").split(",")))
    else:
        sys.stdin.readline()
        target_nums = []
    
    sort = True
    flag = False

    for char in target_p:
        if char == "R":
            sort = not sort
        else:
            if not target_nums:
                flag = True
                break
            if sort:
                target_nums.popleft()
            else:
                target_nums.pop()
    
    if flag:
        print("error")
        continue

    if sort:
        print(str(list(target_nums)).replace(" ", ""))
    else:
        print(str(list(reversed(target_nums))).replace(" ", ""))
     