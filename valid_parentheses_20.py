#Valid Parentheses Leetcode #20
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(' , ']': '[', '}': '{'}
        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            elif c in bracket_map:
                if not stack or stack[-1] != bracket_map[c]:
                    return False
                stack.pop()
            else:
                return False #invalid characters
        return len(stack) == 0
