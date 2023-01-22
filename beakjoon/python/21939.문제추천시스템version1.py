import sys
import heapq

N = int(sys.stdin.readline())
# 어려운 문제가 max_heap[0]
max_heap = []
# 쉬운 문제가 min_heap[0]
min_heap = []
check = dict()
for _ in range(N): 
    num, level = map(int, sys.stdin.readline().split())
    heapq.heappush(min_heap, (level, num))
    heapq.heappush(max_heap, (-level, num))
    check[num] = False

result = ""

M = int(sys.stdin.readline())
for _ in range(M):
    query, *nums = sys.stdin.readline().split()

    if query == "add":
        heapq.heappush(min_heap, (int(nums[1]), int(nums[0])))
        heapq.heappush(max_heap, (-int(nums[1]), int(nums[0])))
        check[int(nums[0])] = False
    
    # 가장 어려운 문제 출력
    elif query == "recommend" and int(nums[0]) == 1: 
        tmp = []
        while max_heap:
            level, num = heapq.heappop(max_heap)
            if not check[num]: 
                check[num] = True
                break
            else: tmp.append((level, num))
        print(-num)
        for level, num in tmp:
            heapq.heappush(max_heap, (level, num))
    
    # 가장 쉬운 문제 출력
    elif query == "recommend" and int(nums[0]) == -1:
        tmp = []
        while min_heap:
            level, num = heapq.heappop(min_heap)
            if not check[num]: 
                check[num] = True
                break
            else: tmp.append((level, num))
        print(num)
        for level, num in tmp:
            heapq.heappush(min_heap, (level, num))
    
    # 문제 제거
    else:
        check[int(nums[0])] = True