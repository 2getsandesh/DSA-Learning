'''First unique character in a string'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            key = s[i]
            if key not in s[i+1:] and key not in s[:i]: return i
        return -1