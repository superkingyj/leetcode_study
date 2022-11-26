import sys

N = int(sys.stdin.readline())
dancing = set()
flag = False

for _ in range(N):
    A, B = sys.stdin.readline().rstrip().split()
    
    # 기록 시작 전
    if not flag and  A != "ChongChong" and B != "ChongChong": 
        continue

    # 기록 시작 후
    if flag:
        if A in dancing or B in dancing:
            dancing.add(A)
            dancing.add(B)
    # 기록 시작 시점
    else:
        flag = True
        dancing.add(A)
        dancing.add(B)

print(len(dancing))