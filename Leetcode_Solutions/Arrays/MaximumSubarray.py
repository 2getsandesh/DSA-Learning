'''Given an integer array nums, find the 
subarray with the largest sum, and return its sum.'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = maxsum = nums[0]
        for i in nums[1:]:
            maxsum = max(i,maxsum+i)
            res = max(res,maxsum)
        return res
        