# Check valid anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t): return True

#-------------------------------------------------------#

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False

        for i in set(s):
            if s.count(i)!=t.count(i): return False
        return True
    
#----------------------------------------------------------#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0]*26
        freq2 = [0]*26
        for i in s:
            freq1[ord(i)-97]+=1
        for i in t:
            freq2[ord(i)-97]+=1
        if freq1 == freq2: return True
        else: return False