class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        left, right = 0, len(needle)
        print(left, right)
        while right <= len(haystack):
            print(haystack[left:right])
            if haystack[left:right] == needle:
                return left
            left += 1
            right += 1
        return -1
