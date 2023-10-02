'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
    

#----------------------------------------------------------#

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)//2
        for key in nums:
            if key in dic:
                dic[key]+=1
            else:
                dic[key]=1

        return max(dic.items(),key= lambda x: x[1])[0]