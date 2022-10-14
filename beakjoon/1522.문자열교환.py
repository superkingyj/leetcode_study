import sys

string = sys.stdin.readline().rstrip()
a_cnt = string.count("a")
min_cnt = sys.maxsize
l = len(string)

for i in range(l):
    tmp_string = ""
    for j in range(i, i+a_cnt):
        tmp_string += string[j%l]
    b_cnt = tmp_string.count("b")
    min_cnt = min(min_cnt, b_cnt)

print(min_cnt)