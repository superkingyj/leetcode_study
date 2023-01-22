import sys

N, M = map(int, sys.stdin.readline().split())
keywords = set(sys.stdin.readline().rstrip() for _ in range(N))
write = list(set(sys.stdin.readline().rstrip().split(",")) for _ in range(M))

for item in write:
    keywords -= item
    print(len(keywords))