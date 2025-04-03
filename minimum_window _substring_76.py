#  Minimum Window Substring  Leet Code #76
class Solution(object):
    def minWindow(self, s, t):
       
        if not s or not t:
            return ""

        required_map = {}
        smallest_window = ""
        formed = 0
        min_len = float("inf")
        for val in t:
            required_map[val] = required_map.get(val, 0) + 1

        required_chars = len(required_map)

        window_map= {}  # Use a hashmap (dictionary) to track the frequency of characters in the current window.
        left = 0  # Start of window
        for right in range(len(s)):
            window_map[s[right]] = window_map.get(s[right], 0) + 1
            
            if s[right] in required_map and window_map[s[right]] == required_map[s[right]]:
                formed += 1

            while formed == required_chars:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    smallest_window = s[left:right + 1]
                window_map[s[left]] -= 1
                if s[left] in required_map and window_map[s[left]] < required_map[s[left]]:
                    formed -= 1
                left = left+1
        return smallest_window if min_len != float("inf") else ""
