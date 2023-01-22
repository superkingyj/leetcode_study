import sys

N, a, b = map(int, sys.stdin.readline().split())

def solve():
    if a+b > N+1: return [-1]
    arr = [1] * 101010
    if a == 1 and b == 1: return arr[1:N+1]
    if a == 1:
        arr[1] = b
        for i in range(1, b):
            arr[N+1-i] = i
        return arr[1:N+1]
    if b == 1:
        p = N+1-a
        for i in range(1, a+1):
            arr[p] = i
            p += 1
        return arr[1:N+1]
    if a <= b:
        p =  N
        for i in range(1, b+1):
            arr[p] = i
            p -= 1
        p = N+2-a-b
        for i in range(1, a):
            arr[p] = i
            p += 1
        return arr[1:N+1]
    else:
        p = N+2-a-b
        for i in range(1,a+1):
            arr[p] = i 
            p += 1
        p = N
        for i in range(1, b):
            arr[p] = i 
            p -= 1
        return arr[1:N+1]

print(*solve())