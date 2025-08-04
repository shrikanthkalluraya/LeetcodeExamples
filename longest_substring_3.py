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

    def longest_substring_without_repeating_characters_using_number_of_occurence(self, s: str) -> int:
        # WRITE YOUR BRILLIANT CODE HERE
        left = 0
        longest_sub_string = ""
        substr_map = {}
        max_len = 0
        for right in range(0, len(s)):
            substr_map[s[right]] = substr_map.get(s[right], 0) + 1 
            while substr_map[s[right]] > 1:
                substr_map[s[left]] -= 1
                left += 1
            curr_max_len = max_len
            max_len = max(max_len, right-left+1)
            if max_len!= curr_max_len:
                longest_sub_string = s[left:right + 1]
        return max_len
