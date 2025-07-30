# 11. Container With Most Water
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right-left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area
