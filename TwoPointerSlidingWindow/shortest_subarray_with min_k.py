'''
Given a positive integer array nums, we want to find the length of the shortest subarray such that the subarray sum is at least target. 
Recall the same example with input nums = [1, 4, 1, 7, 3, 0, 2, 5] and target = 10, 
then the smallest window with the sum >= 10 is [7, 3] with length 2. So the output is 2.
'''
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        left = 0
        min_len = len(nums) + 1
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= k:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_len if min_len <= len(nums) else -1
