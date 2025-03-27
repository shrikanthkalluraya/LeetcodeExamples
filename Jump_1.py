# Jump Problem Leetcode: 55
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) -1
        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
               goal = i
        if goal<= 0:
            return True
        return False
