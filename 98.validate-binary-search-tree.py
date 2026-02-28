#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traverse(root: Optional[TreeNode], low: int, high: int) -> False:
            if root is None:
                return True
            
            if not (low < root.val < high):
                return False

            return traverse(root.left, min(low, root.val), root.val) and \
            traverse(root.right, root.val, max(high, root.val))

        return traverse(root, float('-inf'), float('inf'))

# @lc code=end

