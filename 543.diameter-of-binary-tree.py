#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def traverse(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1
            
            left_depth = traverse(root.left) + 1
            right_depth = traverse(root.right) + 1

            nonlocal ret
            ret = max(ret, left_depth + right_depth)

            return max(left_depth, right_depth)
        
        traverse(root)

        return ret
# @lc code=end

