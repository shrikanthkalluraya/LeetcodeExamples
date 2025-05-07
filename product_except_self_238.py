# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Product of Array Except Self
        prefix = 1
        output=[]
        postfix = 1
        output = [1] * len(nums)  # Initialize output array with 1s

        # First pass: prefix products
        for i in range(len(nums)):
            output[i] = prefix
            prefix = nums[i] * prefix

        # Second pass: postfix products
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i]*  postfix
            postfix = nums[i] *   postfix
        return output
        
