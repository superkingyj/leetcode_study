import sys
from collections import Counter

def check_1():
    global string
    vowel = {'a', 'e', 'i', 'o', 'u'}
    count = Counter(string)
    for key in count.keys():
        if key in vowel: return True
    return False
    
def check_2():
    global string
    vowel = {'a', 'e', 'i', 'o', 'u'}
    l = len(string)
    for i in range(l-2):
        cnt = 0
        for j in range(i, i+3):
            if string[j] in vowel: cnt += 1
        if cnt == 0 or cnt == 3: return False
    return True

def check_3():
    global string
    l = len(string)
    for i in range(l-1):
        if (string[i:i+2] == string[i]*2) and (string[i] != 'e') and (string[i] != 'o'): return False
    return True

while True:
    string = sys.stdin.readline().rstrip()
    
    if string == "end": break

    if not check_1(): print(f"<{string}> is not acceptable."); continue
    if not check_2(): print(f"<{string}> is not acceptable."); continue
    if not check_3(): print(f"<{string}> is not acceptable."); continue
    print(f"<{string}> is acceptable.")
