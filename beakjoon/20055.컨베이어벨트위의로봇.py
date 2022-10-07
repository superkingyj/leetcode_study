import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split())))
robots = deque([0] * N)
time = 0

def move_belt():
    belt.rotate(1)
    robots.rotate(1)

def move_robots():
    if sum(robots) == 0: 
        return

    for i in range(N-2, -1, -1):
        if robots[i]==1 and robots[i+1] ==0 and belt[i+1] > 0:
            robots[i+1] = 1
            robots[i] = 0
            belt[i+1] -= 1

def add_robot():
    if belt[0] > 0 and robots[0] == 0:
        robots[0] = 1
        belt[0] -= 1

def remove_robot():
    robots[-1] = 0

def count_zero():
    return belt.count(0)

while True:
    move_belt()
    remove_robot()
    move_robots()
    remove_robot()
    add_robot()
    time += 1
    
    if count_zero() >= K: break

print(time)

"""
구현
1. 컨베이어 벨트 def move_belt()
    - deque.rotate(1)
2. 로봇 이동 def move_robots()
    - for i in range(N-1):
        if belt[i+1] != 0: 
            robot[i] = 0
            robot[i+1] = robot[i]
3. 로봇 추가 def add_robot()
    - if belt[0] > 0: 
        robot[0] = 1
4. 로봇 삭제 def remove_robot()
    - robot[N-1] = 0
5. zero 내구도 카운트 def count_zero()
    for i in range(N*2):
        if belt[i] == 0: cnt += 1

belt = deque(입력)
robots = [0] * N
cnt = 0 <-- 내구도 cnt
while cnt < K:
    move_belt()
    move_robots()
    add_robots()
    remove_robots()
    coutn_zero()
"""