'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) , len(matrix[0])
        l,r = 0, m-1
        while l<=r:
            mid = (l+r)//2
            if target in matrix[mid]: return True
            elif target > matrix[mid][-1]:
                l = mid+1
            else: r = mid-1
        return False