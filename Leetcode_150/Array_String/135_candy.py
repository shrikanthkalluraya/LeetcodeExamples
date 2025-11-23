class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total = n
        i = 1

        while i < n:

            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            
            upward = 0
            while i < n and ratings[i] > ratings[i-1]:
                upward += 1
                total += upward
                i += 1
            
            if i == n:
                return total
            
            downward = 0 
            while i < n and ratings[i] < ratings[i-1]:
                downward += 1
                total += downward
                i += 1

            total -= min(downward, upward)
        return total
