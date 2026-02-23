#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            left_ret = traverse(root.left)
            right_ret = traverse(root.right)

            return max(left_ret, right_ret) + 1
        
        return traverse(root)
        
# @lc code=end

