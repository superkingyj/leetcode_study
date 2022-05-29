from typing import * 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(i, j):
            i_, j_ = i, j
            s = set()
            for i in range(i, i+3):
                for j in range(j, j+3):
                    if board[i][j] == ".":
                        continue
                    
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
                j = j_
            return True

        for row in board:
            s = set()
            for num in row:
                if num == ".":
                    continue
                    
                if num in s: return False
                else: s.add(num)
        
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                    
                if board[j][i] in s: return False
                else: s.add(board[j][i])
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not isValid(i,j): return False
        return True

sol = Solution()
sol.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]])
            