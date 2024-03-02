class Solution:    
    def isRobotBounded(self, instructions: str) -> bool:
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # N, W, S, E
        dir, x, y = 0, 0, 0
        idx, length = 0, len(instructions)
        
        while idx < length:
            if instructions[idx] == 'L':
                dir = (dir+1) % 4
            elif instructions[idx] == 'R':
                dir = (dir+3) % 4            
            else:
                x, y = x+dxs[dir], y+dys[dir]            
            idx +=1
        
        if (x,y) == (0, 0) or dir != 0: 
            return True
        
        return False
        
        
        