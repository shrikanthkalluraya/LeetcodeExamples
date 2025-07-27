class Solution:
    def can_finish_eating(self, piles, h, k):
        hours_taken = 0
        for pile in piles:
            hours_taken += ceil(float(pile)/k)
        return hours_taken <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        print(max_k)
        left, right, boundary = 0, max_k, -1
        while left <= right:
            mid = (left + right) // 2
            if self.can_finish_eating(piles, h, mid):
                boundary = mid
                right = mid - 1
            else:
                left = mid + 1
        return boundary
        
