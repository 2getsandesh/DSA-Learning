# find the index of needle in haystack. Return -1 if not found

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle,0)
        else:
            return -1