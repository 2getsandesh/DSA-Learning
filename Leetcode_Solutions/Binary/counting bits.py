'''Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
 ans[i] is the number of 1's in the binary representation of i.'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]
        for i in range(1,n+1):
            ans.append(ans[i//2]+i%2)
        return ans
    
#----------------------------------------------------#

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = n*(n+1)//2
        gotsum = sum(nums)
        return actual - gotsum
