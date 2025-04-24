# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')  # Global variable to track max path sum

        def max_gain(node):
            if not node:
                return 0

            # Recursively get max gain from left and right (ignore negative paths)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Price of a new path through this node (could be final answer)
            price_newpath = node.val + left_gain + right_gain

            # Update global max_sum if this path is better
            self.max_sum = max(self.max_sum, price_newpath)

            # Return the max gain that can be extended to parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)  # start recursion
        return self.max_sum
