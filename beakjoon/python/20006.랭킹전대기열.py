import sys

P, M = map(int, sys.stdin.readline().split())
info = [tuple(sys.stdin.readline().split()) for _ in range(P)]
rooms = []

for l, n in info:
    l = int(l)
    flag = False
    
    for i in range(len(rooms)):
        if len(rooms[i][1]) == M:
            continue
            
        if rooms[i][0]-10 <= l <= rooms[i][0]+10:
            flag = True
            rooms[i][1].append((l, n))
            break
    
    if not flag:
        rooms.append([l, [(l, n)]])

for i in range(len(rooms)):
    if len(rooms[i][1]) == M: print("Started!")
    else: print('Waiting!')
    rooms[i][1].sort(key = lambda x:x[1])
    for l, n in rooms[i][1]:
        print(l, n)
    