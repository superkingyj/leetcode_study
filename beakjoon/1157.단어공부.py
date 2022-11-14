import sys
from collections import Counter

s = sys.stdin.readline().rstrip().upper()
count = Counter(s)

max_num, max_cha = 0, []
for key, val in count.items():
    if val == max_num:
        max_cha.append(key)
    elif val > max_num:
        max_num = val
        max_cha = [key]

if len(max_cha) > 1: print("?")
else: print(*max_cha)
