import sys
import heapq

N = int(sys.stdin.readline())
max_heap, min_heap = [], []
check = dict()

for _ in range(N): 
    num, level = map(int, sys.stdin.readline().split())
    check[num] = False
    heapq.heappush(min_heap, (level, num))
    heapq.heappush(max_heap, (-level, -num))

M = int(sys.stdin.readline())
for _ in range(M):
    query, *nums = sys.stdin.readline().split()
    if query == "add":
        while check[-max_heap[0][1]]: heapq.heappop(max_heap)
        while check[min_heap[0][1]]: heapq.heappop(min_heap)    
        check[int(nums[0])] = False
        heapq.heappush(max_heap, (-int(nums[1]), -int(nums[0])))
        heapq.heappush(min_heap, (int(nums[1]), int(nums[0])))

    # 가장 어려운 문제 출력
    elif query == "recommend" and int(nums[0]) == 1: 
        while check[-max_heap[0][1]]:
            heapq.heappop(max_heap)
        print(-max_heap[0][1])
    
    # 가장 쉬운 문제 출력
    elif query == "recommend" and int(nums[0]) == -1:
        while check[min_heap[0][1]]:
            heapq.heappop(min_heap)
        print(min_heap[0][1])
    
    # 문제 제거
    else:
        check[int(nums[0])] = True