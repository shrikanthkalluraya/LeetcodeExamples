# 042 - Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        left = 0
        right = n-1
        water=0
        left_max = height[left]
        right_max = height[right]
        
        while left < right:
            if left_max < right_max:
                left += 1
                if left_max < height[left]:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
            else:
                right -= 1
                if right_max < height[right]:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
        
        return water
