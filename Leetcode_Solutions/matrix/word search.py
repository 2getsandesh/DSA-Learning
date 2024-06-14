'''Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
 The same letter cell may not be used more than once.'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        n = len(word)
        

        def dfs(r,c,i):
            if r<0 or r>=row or c<0 or c>=col or board[r][c] != word[i] : return False

            if i == n-1 and board[r][c] == word[i]: return True

            if board[r][c] == word[i]:
                temp, board[r][c] = board[r][c], '#'
                res = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
                board[r][c] = temp
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0): return True
        return False