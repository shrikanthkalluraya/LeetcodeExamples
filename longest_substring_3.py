# Longest Substring Without Repeating Characters Leet code #3
# Given a string s, find the length of the longest substring without duplicate characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        char_index = {}  # Store last seen index of characters
        left = 0  # Start of window
        max_length = 0  # Result
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # Move left past duplicate
            char_index[s[right]] = right  # Update last seen index
            max_length = max(max_length, right - left + 1)  # Update max_length    
        return max_length
