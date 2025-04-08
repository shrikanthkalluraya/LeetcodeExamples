# Maximum Subarray Leetcode #53
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
