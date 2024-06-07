'''Given an integer array nums, return the length of the longest strictly increasing 
subsequence'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        li = [1]*n

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    li[i] = max(li[i], 1+li[j])
        return max(li)