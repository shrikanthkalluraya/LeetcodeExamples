# Sliding Window Maximum Leetcode #239
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

#Return the max sliding window.

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        result = []
        dq = deque()  # store indices
        for i in range(len(nums)):
            # 1. Remove indices out of current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. Remove smaller values from the back
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Append max value when window size is reached
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
