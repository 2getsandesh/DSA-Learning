# find the index of needle in haystack. Return -1 if not found

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle,0)
        else:
            return -1
        

#--------------------------------------------------------------#

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j=0,len(needle)
        while j<=len(haystack):
            curr = haystack[i:j]
            if curr==needle: return i
            else:
                i+=1
                j+=1
        return -1