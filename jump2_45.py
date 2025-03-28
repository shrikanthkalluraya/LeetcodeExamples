#Jump 2 Leetcode - 45
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize variables: jumps, current jump range, and farthest reach
        if lens(nums)==1:
          return 0
        jumps = 0
        far = 0
        curr_end=0
        
        # Loop through the array
        for idx in range(len(nums)-1):
            # Update the farthest we can reach
            far = max(far, nums[idx] + idx)
            if curr_end==idx:
                jumps+=1
                curr_end=far

            if curr_end>=len(nums)-1:
                break
        return jumps
