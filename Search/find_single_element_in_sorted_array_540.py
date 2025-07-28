# 540. Single Element in a Sorted Array
'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def has_no_dupicate_element(idx):
            if idx == len(nums) - 1:
                return True
            elif (idx%2):
                #its an odd number
                return nums[idx] != nums[idx - 1]
            else:
                #its an even number
                return nums[idx] != nums[idx + 1]


        left, right, boundary = 0, len(nums) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if has_no_dupicate_element(mid):
                boundary = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[boundary]
