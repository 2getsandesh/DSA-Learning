'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
                

#-----------------Hash Table----------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]]=i

        for i in range(n):
            comp = target - nums[i]
            if comp in numMap and numMap[comp]!=i:
                return [i,numMap[comp]]
            
#------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums and nums.index(comp) != i: return [i,nums.index(comp)]