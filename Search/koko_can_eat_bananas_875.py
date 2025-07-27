# 875. Koko Eating Bananas
'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

'''

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
        
