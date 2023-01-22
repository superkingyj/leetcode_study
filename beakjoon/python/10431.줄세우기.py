import sys


P = int(sys.stdin.readline())
result = ""

for _ in range(P):
    arr = list(map(int, sys.stdin.readline().split()))
    T = arr[0]
    cnt, max_num = 0, 0
    sorted = []

    for i in range(1,21):
        if max_num < arr[i]: 
            sorted.append(arr[i])
            max_num = max(max_num, arr[i])
        else:
            idx = 0 
            while True:
                if sorted[idx] > arr[i]:
                    cnt += len(sorted) - idx
                    sorted.insert(idx, arr[i])
                    break
                idx += 1

    result += str(T) + " " + str(cnt) + "\n"

print(result[:-1])