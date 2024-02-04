import sys

N = int(sys.stdin.readline())
enter, out = {}, []

for i in range(N):
    car = sys.stdin.readline().rstrip()
    enter[car] = i

for _ in range(N):
    car = sys.stdin.readline().rstrip()
    out.append(car)

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if enter[out[i]] > enter[out[j]]:
            cnt += 1
            break

print(cnt)
