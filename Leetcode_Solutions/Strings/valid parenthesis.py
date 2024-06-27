'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

class Solution:
    def isValid(self, s: str) -> bool:
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        stack = []
        
        for i in s:
            stack.append(i)
            if len(stack)>1: 
                prev = stack[-2]
                top = stack[-1]
                if prev in left and top in right and left.index(prev) == right.index(top):
                    stack.pop()
                    stack.pop()
        return False if stack else True

#-----------------------------------------------------------------------------#
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        while n>0:
            initial = len(s)
            s=s.replace('()','').replace('{}','').replace('[]','')
            n = len(s)
            if initial == n: return False
        return True
#-----------------------------------------------------------------------------#
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 != 0 : return False
        openb = ['(','[','{']
        closeb = [')',']','}']
        li = []

        l = r = 0
        for r in range(n):
            if s[r] in openb: li.append(openb.index(s[r]))
            elif s[r] in closeb: 
                if li and closeb.index(s[r]) == li[-1]:
                    li.pop()
                else: return False
        if li == []: return True

