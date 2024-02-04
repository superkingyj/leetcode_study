import sys

for _ in range(3):
    cnt = sum(list(map(int, sys.stdin.readline().split())))
    if cnt == 0:
        print("D")
    elif cnt == 1:
        print("C")
    elif cnt == 2:
        print("B")
    elif cnt == 3:
        print("A")
    else:
        print("E")
