# Leetcode Problem - 1
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_map:
                return [num_map[diff],idx]
            num_map[num] = idx
        return []
