#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    #     def traverse(root: 'TreeNode'):
    #         if root is None:
    #             return None
            
    #         if root.val in (p.val, q.val):
    #             return root
            
    #         left = traverse(root.left)
    #         right = traverse(root.right)

    #         if left and right:
    #             return root
            
    #         return left or right
        
    #     return traverse(root)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root

        while True:
            if current_node.val < p.val and current_node.val < q.val:
                current_node = current_node.right
            elif current_node.val > p.val and current_node.val > q.val:
                current_node = current_node.left
            else:
                return current_node
        
# @lc code=end

