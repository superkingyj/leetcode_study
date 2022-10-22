import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
words = defaultdict(int)

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        words[word] += 1

words = list(words.items())
words.sort(key = lambda x:(-x[1], -len(x[0]), x))
for key, val in words:
    print(key)