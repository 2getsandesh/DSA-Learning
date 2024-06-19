'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = collections.Counter(nums)
        sorted_list = sorted(numMap.items(),key= lambda x: x[1], reverse=True)
        li = [i[0]  for i in sorted_list[:k]]
        return li