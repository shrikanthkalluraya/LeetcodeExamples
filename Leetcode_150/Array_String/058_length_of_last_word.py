class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        idx = (s.rfind(' ')) + 1
        return len(s[idx:])
