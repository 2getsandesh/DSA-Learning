'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
 You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=longest = 0
        freq = [0]*26

        for r in range(len(s)):
            
            freq[ord(s[r])-65] += 1
            while (r-l+1) - max(freq)>k: 
                freq[ord(s[l])-65] -= 1
                l+=1
            longest = max(r-l+1, longest)
        return longest


#-------------------------more efficient-------------------------------------#
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxcount = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            windowlen = r-l+1
            if windowlen-max(freq.values()) > k:
                freq[s[l]] -= 1
                l+=1
            else: maxcount = max(windowlen,maxcount)
        return maxcount