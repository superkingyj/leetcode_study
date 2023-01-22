import sys

V, E = map(int, sys.stdin.readline().split())

parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

edges = []
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort()

def find(parent, x):
    if parent[x] == x: return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

result = 0
for c, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c

print(result)
