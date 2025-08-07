# 76. Minimum Window Substring
'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1
        
        required = len(need)
        formed = 0

        window_chars = {}
        min_len = float('inf')
        min_left = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_chars[char] = window_chars.get(char, 0) + 1
            if char in need and need[char] == window_chars[char]:
                formed += 1

            while left <= right and formed == required:
                if right-left+1 < min_len:
                    min_len = right-left+1
                    min_left = left
                
                char = s[left]
                window_chars[char] -= 1

                if char in need and need[char] > window_chars[char]:
                    formed -= 1

                left += 1
            right += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_left: min_left+min_len]



        
