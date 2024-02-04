import sys

T = int(sys.stdin.readline())

for _ in range(T):
    W, N = map(int, sys.stdin.readline().split())
    curr_weight, total_dist, curr_pos = 0, 0, 0
    
    for _ in range(N):
        x_i, w_i = map(int, sys.stdin.readline().split())
        # 현재 쓰레기의 양이 용량에 도달했다면
        if curr_weight == W:
            # 쓰레기장에 돌아갔다가 다시 옴
            total_dist += 2 * curr_pos
            curr_weight = 0

        # 현재 지점을 이동
        total_dist += (x_i - curr_pos)
        curr_pos = x_i
        # 그 지점의 쓰레기를 실었을 때 용량이 넘는다면
        if curr_weight + w_i > W:
            total_dist += 2 * curr_pos
            curr_weight = w_i
        # 아니라면 쓰레기 싣고 이동 
        else:
            curr_weight += w_i
    
    # 더 이상 쓰레기를 실을 지점이 없음
    total_dist += curr_pos
    print(total_dist)