# Leetcode: 347. Top K Frequent Elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Step 1: Count frequencies using a Counter or dictionary
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Use a min-heap of size k
        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))  # Push tuple (frequency, number)
            if len(heap) > k:
                heapq.heappop(heap)  # Remove smallest frequency element


        # Step 3: Extract the elements from the heap
        return [num for count, num in heap]
