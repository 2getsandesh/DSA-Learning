'''Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxpro = minpro = nums[0]
        for i in nums[1:]:
            tempmin = min(i,minpro*i,maxpro*i)
            tempmax = max(i,minpro*i,maxpro*i)
            maxpro, minpro = tempmax,tempmin
            res = max(res,maxpro)
        return res