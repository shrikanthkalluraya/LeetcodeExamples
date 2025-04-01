# Longest Substring with At Most K Distinct Characters  Leet code #340
class Solution(object):
    def lengthOfLongestSubstringWithKdistinct(self, s, k):
        if k == 0 or s == "":
         return 0

        char_freq= {}  # Use a hashmap (dictionary) to track the frequency of characters in the current window.
        left = 0  # Start of window
        max_length = 0  # Result
        for right in range(len(s)):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1  
            while len(char_freq) > k:
                char_freq[s[left]] -= 1
                if char_freq[s[left]] == 0:
                    del char_freq[s[left]] 
                left = left + 1
            max_length = max(max_length, right - left + 1)
        return max_length
