'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1: return nums[0]
        
        def maxfinder(nums: List[int]) -> int:
            n = len(nums)
            if n==0 : return 0
            if n==1: return nums[0]
            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            for i in range(2,n):
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
            return dp[n-1] 
        
        return max(maxfinder(nums[1:]), maxfinder(nums[:l-1]))