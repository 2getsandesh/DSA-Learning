'''Given a string s, find the length of the longest 
substring without repeating characters.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = longest = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            longest=max(longest,r-l+1)
        return longest
