import sys

T = int(sys.stdin.readline())
results = []

def backtracking(s, idx):
    global results
    
    if idx >= len(s):
        raw_exp = "".join(s)
        edit_exp = raw_exp.replace(" ", "")
        if eval(edit_exp) == 0: results.append(raw_exp)
        return
    
    s[idx] = "+"
    backtracking(s, idx+2)

    s[idx] = " "
    backtracking(s, idx+2)

    s[idx] = "-"
    backtracking(s, idx+2)

for _ in range(T):
    N = int(sys.stdin.readline())
    s = []
    for i in range(1,N+1):
        s.append(str(i))
        if i != N: s.append("o")
    
    backtracking(s, 1)
    results.sort()
    for result in results:
        print(result)
    print()
    results = []