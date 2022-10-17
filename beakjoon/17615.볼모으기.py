import sys

N = int(sys.stdin.readline())
balls = sys.stdin.readline().rstrip()
min_cnt = sys.maxsize

new_balls = balls.rstrip("R")
min_cnt = min(min_cnt, new_balls.count("R"))
new_balls = balls.rstrip("B")
min_cnt = min(min_cnt, new_balls.count("B"))
new_balls = balls.lstrip("R")
min_cnt = min(min_cnt, new_balls.count("R"))
new_balls = balls.lstrip("B")
min_cnt = min(min_cnt, new_balls.count("B"))
print(min_cnt)