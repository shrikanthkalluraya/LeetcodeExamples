# 169 - Majority Element
# https://leetcode.com/problems/majority-element/

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = c.most_common(1)
        return m[0][0]
