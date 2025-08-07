# 1537. Get the Maximum Score
'''
You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

Choose array arr1 or arr2 to traverse (from index-0).
Traverse the current array from left to right.
If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
The score is defined as the sum of unique values in a valid path.

Return the maximum score you can obtain of all possible valid paths. Since the answer may be too large, return it modulo 109 + 7.

 
'''

class Solution:
    def maxSum(self, arr1: List[int], arr2: List[int]) -> int:
        i, j = 0, 0
        sum1, sum2 = 0, 0
        result = 0
        mod = 10**9 + 7
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
                
            elif arr2[j] < arr1[i]:
                sum2 += arr2[j]
                j += 1
            else:
                result += max(sum1,sum2) + arr1[i]
                sum1,sum2=0, 0
                i += 1
                j += 1
            
        
        
        while i < len(arr1):
            sum1 += arr1[i]
            i += 1
        
        while j < len(arr2):
            sum2 += arr2[j]
            j += 1
        
        result += max(sum1, sum2)
        return result % mod
