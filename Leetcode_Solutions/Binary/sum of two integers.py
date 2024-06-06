'''Given two integers a and b, return the sum of the two integers without using the operators + and -.'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        
        #ends loop when "mask&b" becomes 0. But b might still contain 1111... if initial b was negative
        while mask&b > 0: 
            a,b = a^b, (a&b)<<1
        return mask&a if b>0 else a

        #if initial b was negative, then after the loop, b will still contain some 111.... 
        #hence mask&a should be returned else 'a' is returned