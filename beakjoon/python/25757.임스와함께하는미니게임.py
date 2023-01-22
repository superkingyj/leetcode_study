import sys

d = {
    'Y':2,
    'F':3,
    'O':4
}

N, G = sys.stdin.readline().split()
num = d[G]
people = set()
[people.add(sys.stdin.readline().rstrip()) for _ in range(int(N))]

print(len(people) // (num-1))