class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()  # sort the citations from smallest to biggest
        n = len(citations)
        h = 0
        
        for i in range(n):
            # number of papers that have at least citations[i] = n - i
            if citations[i] >= n - i:
                h = n - i
                break
        return h
