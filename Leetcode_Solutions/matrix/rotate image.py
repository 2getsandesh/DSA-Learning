'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        first, last = 0, n-1
        while first<last:
            matrix[first], matrix[last] = matrix[last], matrix[first]
            first += 1
            last -= 1

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        
        return matrix
