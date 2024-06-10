'''You are given an integer array height of length n.
 There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r,area = 0,n-1,0

        while l<r:
            minheight = min(height[r],height[l])
            area = max(area,minheight*(r-l))

            if height[r]>height[l]: l+=1
            else: r-=1
        return area
    