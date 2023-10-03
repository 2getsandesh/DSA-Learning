'''Return True if it contains duplicate'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        if len(new) == len(nums): return False
        else: return True

#-----------------------------------------------------------#

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
#-----------------------------------------------------------#

