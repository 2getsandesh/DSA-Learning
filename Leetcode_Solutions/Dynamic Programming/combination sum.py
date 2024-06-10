'''Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = candidates
        n = len(nums)
        cur = []

        def dfs(i, cur, total):
            if total == target: 
                res.append(cur[:])
                return

            if total>target or i>=n: return

            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0,cur,0)
        return res