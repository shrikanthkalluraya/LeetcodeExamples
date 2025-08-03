'''
Recall finding the largest size k subarray sum of an integer array in Largest Subarray Sum. What if we don't need the largest sum among all subarrays of fixed size k, but instead, we want to find the length of the longest subarray with sum smaller than or equal to a target?

Given input nums = [1, 6, 3, 1, 2, 4, 5] and target = 10, then the longest subarray that does not exceed 10 is [3, 1, 2, 4], so the output is 4 (length of [3, 1, 2, 4]).
'''
class Solution:
    def subarraySumlongest(nums: list[int], target: int) -> int:
        left = 0
        max_len = 0
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum > target:
                window_sum -= nums[left]
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len
