# 125. Valid Palindrome
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
         arr = [c.lower() for c in s if c.isalnum()]
         left, right = 0, len(arr) - 1
         while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
         return True
