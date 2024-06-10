'''Write a function that takes the binary representation of an unsigned integer and 
returns the number of '1' bits it has (also known as the Hamming weight).'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        count = 0
        for i in s:
            if i == '1':
                count += 1
        return count
    
#-------------------------------------------------------------------#

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            if n&1 == 1: c += 1
            n = n>>1
        return c
        