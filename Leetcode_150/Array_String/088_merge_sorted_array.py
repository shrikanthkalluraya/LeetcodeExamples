# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        id1 = m - 1
        id2 = n - 1
        right = m + n - 1
        
        while id2 >= 0:
            if id1 >= 0 and nums1[id1] > nums2[id2]:
                nums1[right] = nums1[id1]
                id1 -= 1
            else:
                nums1[right] = nums2[id2]
                id2 -= 1
            right -= 1
