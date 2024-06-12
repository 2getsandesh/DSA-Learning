'''Given an m x n integer matrix matrix, if an element is 0,
 set its entire row and column to 0's.
You must do it in place.'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        rlist = []
        clist = []

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    rlist.append(r) 
                    clist.append(c) 
        
        for r in rlist:
            for i in range(col):
                matrix[r][i]=0 
        for c in clist:
            for i in range(row):
                matrix[i][c]=0 

        return matrix
                


