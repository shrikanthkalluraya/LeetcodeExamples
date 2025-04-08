# Merge Intervals LeetCode #56
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda x: x[0])

        merged_list = [intervals[0]]

        for interval in intervals[1:]:
            last_merged_interval = merged_list[-1]
            if interval[0] <= last_merged_interval[1]:
                last_merged_interval[1] = max(last_merged_interval[1], interval[1])
            else:
                merged_list.append(interval)
        return merged_list
        
