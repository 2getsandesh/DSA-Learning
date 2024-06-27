'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stop when openN == closeN == n
        # add open bracket if openN < n
        # add close bracket if closeN < openN

        stack = []
        res = []
        def generate(openN,closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return
                
            if openN < n:
                stack.append('(')
                generate(openN+1,closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(')')
                generate(openN,closeN+1)
                stack.pop()
        generate(0,0)
        return res