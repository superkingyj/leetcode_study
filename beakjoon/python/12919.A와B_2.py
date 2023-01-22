import sys

def backtracking(t):
    global flag

    if t == S:
        flag = True
        return
    if not t:
        return
    
    if t[-1] == 'A':
        backtracking(t[:-1])
    if t[0] == "B":
        backtracking(t[1:][::-1])


S = list(map(str, sys.stdin.readline().strip()))
T = list(map(str, sys.stdin.readline().strip()))
flag = False
backtracking(T)

print(1 if flag else 0)
