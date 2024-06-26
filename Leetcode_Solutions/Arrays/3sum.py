'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)-2):
            j,k = i+1, len(nums)-1
            while j<k:
                currsum = nums[j] + nums[k] + nums[i]
                if currsum == 0: 
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif currsum > 0: k-=1
                else: j+=1
        return res