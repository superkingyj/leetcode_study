import sys

M = int(sys.stdin.readline())
S = [0] * 21

for _ in range(M):
    qry = sys.stdin.readline().rstrip().split()

    if qry[0] == "add":
        S[int(qry[1])] = 1
    elif qry[0] == "check":
        if S[int(qry[1])] == 1:
            print(1)
        else: 
            print(0)
    elif qry[0] == "remove":
        S[int(qry[1])] = 0
    elif qry[0] == "toggle":
        if S[int(qry[1])] == 1:
            S[int(qry[1])] = 0
        else:
            S[int(qry[1])] = 1
    elif qry[0] == "all":
        for i in range(1, 21):
            S[i] = 1
    else:
        for i in range(1, 21):
            S[i] = 0