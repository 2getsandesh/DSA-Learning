'''You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        one,two=1,1
        for i in range(2,n+1):
            temp=one+two
            one=two
            two=temp
        return two
    
#-----------------------------------------------------------#
    
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:return 1
        if n==2: return 2
        dp = [0]*(n)
        dp[0],dp[1] = 1,2
        
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]