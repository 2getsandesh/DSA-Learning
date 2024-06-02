'''Given an integer array nums, find the 
subarray with the largest sum, and return its sum.'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = nums[0]
        maxsum = nums[0]

        for i in nums[1:]:
            currsum = max(i, currsum + i)
            maxsum = max(maxsum, currsum)
        return maxsum
        