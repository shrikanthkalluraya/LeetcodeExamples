# Largest Rectangle in Histogram Leetcode #84
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        main_stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):

            while main_stack and heights[i] < heights[main_stack[-1]]:
                top_index = main_stack.pop()
                height = heights[top_index]
                # Width is i if main_stack is empty, else i - main_stack[-1] - 1
                width = i if not main_stack else i - main_stack[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            main_stack.append(i)

        return max_area
