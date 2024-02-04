import sys

king_pos, stone_pos, N = sys.stdin.readline().rstrip().split()
dir_info = {
    # dir[move] = [x_dir, y_dir]
    "R": [0, 1],
    "L": [0, -1],
    "B": [1, 0],
    "T": [-1, 0],
    "RT": [-1, 1],
    "LT": [-1, -1],
    "RB": [1, 1],
    "LB": [1, -1]
}

arr_to_chess_x = { 0:'8', 1:'7', 2:'6', 3:'5', 4:'4', 5:'3', 6:'2', 7:'1'}
arr_to_chess_y = { 0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}

chess_to_arr_x = {'8':0, '7':1, '6':2, '5':3, '4':4, '3':5, '2':6, '1':7}
chess_to_arr_y = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def get_dir(dir):
    return dir_info[dir]  

def in_range(x, y):
    return 0 <= x < 8 and 0 <= y < 8

king_x, king_y = chess_to_arr_x[king_pos[1]], chess_to_arr_y[king_pos[0]]
stone_x, stone_y = chess_to_arr_x[stone_pos[1]], chess_to_arr_y[stone_pos[0]]
for _ in range(int(N)):
    dir = sys.stdin.readline().rstrip()
    x_dir, y_dir = get_dir(dir)
    new_king_x, new_king_y = king_x + x_dir, king_y + y_dir
    
    # 만약 새로운 이동위치가 돌과 같은 곳이라면
    if new_king_x == stone_x and new_king_y == stone_y:
        new_stone_x, new_stone_y = stone_x + x_dir, stone_y + y_dir
        # 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너뛴다
        if (not in_range(new_king_x, new_king_y)) or (not in_range(new_stone_x, new_stone_y)): continue
        king_x, king_y = new_king_x, new_king_y
        stone_x, stone_y =new_stone_x, new_stone_y
    # 아니라면
    else:
        # 킹이 체스판 밖으로 나갈 경우에는 그 이동은 건너뛴다
        if not in_range(new_king_x, new_king_y): continue
        king_x, king_y = new_king_x, new_king_y

print(arr_to_chess_y[king_y]+arr_to_chess_x[king_x])
print(arr_to_chess_y[stone_y]+arr_to_chess_x[stone_x])