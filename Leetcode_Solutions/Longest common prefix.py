'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".'''

class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        ans=''
        s=sorted(s)
        f,l=s[0],s[-1]
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                return ans
            ans+=f[i]
        return ans