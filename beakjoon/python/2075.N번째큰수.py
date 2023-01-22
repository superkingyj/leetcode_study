import sys
import heapq

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    for i in map(int, sys.stdin.readline().rstrip().split()):
        heapq.heappush(num, i)
        if len(num) > N:
            heapq.heappop(num)

print(heapq.heappop(num))

