class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        if numRows == 1:
            return s
        r = 0
        idx = 0
        asc = True
        for char in s:
            rows[r].append(char)
            if r == numRows - 1:
                asc = False
            elif r == 0:
                asc = True
            if asc:
                r += 1
            else:
                r -= 1
            idx += 1
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        return "".join(rows)
