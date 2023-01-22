import sys

N, K, P, X = map(int, sys.stdin.readline().split())

d = {
    #   0 1 2 3 4 5 6 7 8 9
    0: (0,4,3,3,4,3,2,3,1,2),
    1: (4,0,5,3,2,5,6,1,5,4),
    2: (3,5,0,2,5,4,3,4,2,3),
    3: (3,3,2,0,3,2,3,2,2,1),
    4: (4,2,5,3,0,3,4,3,3,2),
    5: (3,5,4,2,3,0,1,4,2,1),
    6: (2,6,3,3,4,1,0,5,1,2),
    7: (3,1,4,2,3,4,5,0,4,3),
    8: (1,5,2,2,3,2,1,4,0,1),
    9: (2,4,3,1,2,1,2,3,1,0)
}

digit = len(str(N))
x = str(X).zfill(digit)
total_cnt = 0
for i in range(1, N+1):
    n = str(i).zfill(digit)
    cnt = 0
    for _n, _x in zip(n, x):
        cnt += d[int(_n)][int(_x)]
    if i != X and cnt <= P :
        total_cnt += 1
    
print(total_cnt)