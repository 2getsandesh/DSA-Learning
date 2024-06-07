"Reverse bits of a given 32 bits unsigned integer."

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res<<1
            res = res | n&1
            n=n>>1
        return res
    
class Solution:
    def reverseBits(self, n: int) -> int:
        st = bin(n)[2:].zfill(32)
        return int(st[::-1],2)