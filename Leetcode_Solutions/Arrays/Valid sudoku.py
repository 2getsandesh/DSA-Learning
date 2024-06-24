'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c]) 
                cols[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
    

#==========================================================================================================================#

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        square = {(i, j): set() for i in range(3) for j in range(3)}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c]) 
                cols[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True