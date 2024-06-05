'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}

        for string in strs:
            key = ''.join(sorted(string))
            if key in groupMap: groupMap[key].append(string)
            else: groupMap[key] = [string]
        return list(groupMap.values())