#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret = True

        def traverse(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)

            nonlocal ret
            if abs(left - right) > 1:
                ret = False

            return max(left, right) + 1
        
        traverse(root)

        return ret
    
        
        
# @lc code=end

