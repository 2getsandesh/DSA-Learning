'''Given an array of integers temperatures represents the daily temperatures, return an array answer such that
 answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
 If there is no future day for which this is possible, keep answer[i] == 0 instead.'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([i,temp])
        return res

            
            
