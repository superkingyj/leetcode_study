import sys
winner_sum = 0
winner_num = -1

for i in range(5):
    sum_ = sum(list(map(int, sys.stdin.readline().split())))
    if winner_sum < sum_:
        winner_sum = sum_
        winner_num = i

print(winner_num+1, winner_sum)