#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        path = []

        def traverse(root: Optional[TreeNode], path: list):
            if len(path) == k:
                return 
            
            if root is None:
                return

            traverse(root.left, path)
            path.append(root)
            traverse(root.right, path)

        traverse(root, path)

        return path[k - 1].val
            

        
# @lc code=end

