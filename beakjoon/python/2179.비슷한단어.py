import sys
from collections import defaultdict

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
trie = defaultdict(dict)
d = defaultdict(int)
idxs = defaultdict(list)
p_lst = []

def dfs(idx, s, head, p, i):
    d[p] += 1
    idxs[p].append(i)
    
    if idx >= len(s): 
        return
    
    head[s[idx]] = dict()
    dfs(idx+1, s, head[s[idx]], p+s[idx], i)

for i, s in enumerate(arr):
    dfs(0, s, trie[""], "", i)

max_len, prefix = 0, 0
for key, val in d.items():
    if val <= 1: continue
    if key == "": continue
    
    if max_len < len(key):
        max_len = len(key)
        prefix = key

for i in range(2):
    print(arr[idxs[prefix][i]])
