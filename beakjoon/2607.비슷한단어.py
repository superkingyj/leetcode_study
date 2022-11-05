import sys

N = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
strings = set()
arr = [sys.stdin.readline().rstrip() for _ in range(N-1)]
cnt = 0

def init():
    global strings

    s = list(string)
    s.sort()
    strings.add(tuple(s))

    for val in range(65, 91):
        s = list(string)
        s.append(chr(val))
        s.sort()
        strings.add(tuple(s))
    
    for i in range(len(string)):
        s = list(string)
        del s[i]
        s.sort()
        strings.add(tuple(s))
    
    for i in range(len(string)):
        for val in range(65, 91):
            if string[i] == chr(val): continue
            s = list(string)
            s[i] = chr(val)
            s.sort()
            strings.add(tuple(s))

init()
for item in arr:
    item = list(item)
    item.sort()
    if tuple(item) in strings: cnt += 1

print(cnt)