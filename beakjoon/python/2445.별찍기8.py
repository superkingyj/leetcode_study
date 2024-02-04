import sys

N = int(sys.stdin.readline())

for star_cnt in range(1, N+1):
    middle_space_cnt = 2*N - 2*star_cnt
    print("*"*star_cnt + " "*middle_space_cnt + "*"*star_cnt)

for star_cnt in range(N-1, 0, -1):
    middle_space_cnt = 2*N - 2*star_cnt
    print("*"*star_cnt + " "*middle_space_cnt + "*"*star_cnt)