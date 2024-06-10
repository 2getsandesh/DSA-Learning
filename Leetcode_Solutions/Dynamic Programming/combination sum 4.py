'''Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(target+1):
            for num in nums:
                if num<=i:
                    dp[i] += dp[i-num]
        return dp[target]
