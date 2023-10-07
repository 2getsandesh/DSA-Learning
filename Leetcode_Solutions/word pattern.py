'''Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        a = list(pattern)
        b = list(s.split(' '))
        if len(a)!= len(b): return False
        dic = {}

        for i,j in zip(a,b):
            if i in dic:
                if dic[i] != j: return False
            else:
                if j in dic.values(): return False
                else: dic[i] = j
        return True
    


    #----------------------------------------------------------#



class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        a = list(pattern)
        b = list(s.split(' '))
        if len(a)!= len(b): return False
        if len(set(a))!= len(set(b)): return False
        dic = {}

        for i,j in zip(a,b):
            if i in dic:
                if dic[i] != j: return False
            else:
                dic[i] = j
        return True 