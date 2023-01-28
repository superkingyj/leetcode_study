import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().split())
tree = dict()

def dfs(node):
    global files, cnt

    if node not in tree: return

    for _node, num in tree[node]:
        if num == 0:
            files.add(_node)
            cnt += 1
        else:
            dfs(_node)

for _ in range(N+M):
    P, F, C = sys.stdin.readline().rstrip().split()
    if P not in tree:
        tree[P] = []
    tree[P].append((F, int(C)))

Q = int(sys.stdin.readline())
for _ in range(Q):
    files, cnt = set(), 0
    query = list(sys.stdin.readline().rstrip().split("/"))
    dfs(query.pop())
    print(len(files), cnt)