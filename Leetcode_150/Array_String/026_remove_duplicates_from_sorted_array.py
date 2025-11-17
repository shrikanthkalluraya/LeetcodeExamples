# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for k in range(1, len(nums)):
            if nums[k] != nums[i - 1]:
                nums[i] = nums[k]
                i += 1
        return i
