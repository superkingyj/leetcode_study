import sys

def in_range(x):
    return 0 <= x < 9

def check(x, type, grid):
    d = [1, 3, 4, 2]
    
    for i in range(4):
        cnt, new_x = 0, x
        for _ in range(3):
            new_x += d[i]
            if in_range(new_x):
                if grid[new_x] == type: cnt += 1
            else: break
        if cnt == 3: return True
    
    return False          

def is_valid(grid):
    return "".join(grid) == input

def backtracking(turn, combi, x_idx, o_idx):
    global result

    # 게임 끝
    type = "O" if turn % 2 else "#"
    for i in range(9):
        if check(i, type, combi): 
            if is_valid(combi): result = "valid"
            return
    
    null_cnt = 0
    for i in range(9):
        if combi[i] == ".": null_cnt += 1
    if null_cnt == 0: return 

    if turn > 9:
        if result == "valid": return
        if is_valid(combi): result = "valid"
        return

    # X차례
    if (turn % 2) == 0:
        if x_idx < len(x_idxs):
            for idx in range(x_idx, len(x_idxs)):
                combi[x_idxs[idx]] = "X"
                backtracking(turn+1, combi, idx+1, o_idx)
                combi[x_idxs[idx]] = "."
        else: backtracking(turn+1, combi, x_idx, o_idx)

    # O차례
    else:
        if o_idx < len(o_idxs):
            for idx in range(o_idx, len(o_idxs)):
                combi[o_idxs[idx]] = "O"
                backtracking(turn+1, combi, x_idx, idx+1)
                combi[o_idxs[idx]] = "."
        else: backtracking(turn+1, combi, x_idx, o_idx)

while True:
    result = "invalid"
    input = sys.stdin.readline().rstrip()
   
    if input == "end": break
    
    x_idxs, o_idxs = [], []
    for i in range(9):
        if input[i] == "O": o_idxs.append(i)
        elif input[i] == "X": x_idxs.append(i)

    backtracking(0, ["."]*9, 0, 0)
    print(result)


"""
XXX
OO.
XXX

XOX
OXO
XOX

OXO
XOX
OXO
"""