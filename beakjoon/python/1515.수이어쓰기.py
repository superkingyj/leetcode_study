import sys

string = sys.stdin.readline().rstrip()
idx = 0
flag = False

for i in range(1, 300000000):
    num = str(i)
    for j in range(len(num)):
        if string[idx] == num[j]:
            idx += 1
        if idx == len(string):
            flag = True
            break
    
    if flag: break

print(i)
