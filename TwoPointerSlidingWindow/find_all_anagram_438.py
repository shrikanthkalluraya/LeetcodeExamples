# 438. Find All Anagrams in a String
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
'''
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res

        p_counter = Counter(p)
        window_counter = Counter(s[:len(p)])

        if p_counter == window_counter:
            res.append(0)

        for i in range(len(p), len(s)):
            window_counter[s[i - len(p)]] -= 1
            if window_counter[s[i - len(p)]] == 0:
                del window_counter[s[i - len(p)]]

            window_counter[s[i]] += 1

            if p_counter == window_counter:
                res.append(i - len(p) + 1)

        return res
