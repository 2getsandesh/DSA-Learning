'''First unique character in a string'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            key = s[i]
            if key not in s[i+1:] and key not in s[:i]: return i
        return -1
    
#-------------------------------------------------------------------#

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i)==1: return s.index(i)
        return -1