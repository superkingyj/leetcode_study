import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
light = 0

for _ in range(M):
    q, s, e = map(int, sys.stdin.readline().split())
    if q == 1:
        if e == 1:
            light |= (1 << s)
        else:
            light &= ~(1 << s)
    elif q == 2:
        for i in range(s, e+1):
            light ^= (1 << i)
    elif q == 3:
        for i in range(s, e+1):
            light &= ~(1 << i)
    else: 
        for i in range(s, e+1):
            light |= (1 << i)
    
light |= (1 << N+2)
print("".join(reversed(bin(light)))[1:N+1])
print(bin(light)[-2:-(N+2):-1])

# for _ in range(M):
#     q, s, e = map(int, sys.stdin.readline().split())
#     if q == 1:
#         arr[s-1] = e
#     elif q == 2:
#         for i in range(s-1, e):
#             arr[i] = int(not arr[i])
#     elif q == 3:
#         for i in range(s-1, e):
#             arr[i] = 0
#     else: 
#         for i in range(s-1, e):
#             arr[i] = 1

# print(*arr)