#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse(root: Optional[TreeNode]):
            if root is None:
                return

            traverse(root.left)
            traverse(root.right)
            
            root.left, root.right = root.right, root.left

        traverse(root)

        return root
        
# @lc code=end

