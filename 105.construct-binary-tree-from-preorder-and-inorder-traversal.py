#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def make_tree(sub_preorder: List[int], sub_inorder: List[int]):
            if len(sub_preorder) == 0 or len(sub_inorder) == 0:
                return None
            
            root = TreeNode(sub_preorder[0])
            inorder_index = sub_inorder.index(root.val)

            root.left = make_tree(sub_preorder[1: inorder_index + 1], sub_inorder[:inorder_index])
            root.right = make_tree(sub_preorder[inorder_index + 1:], sub_inorder[inorder_index + 1:])

            return root
        
        return make_tree(preorder, inorder)
        

# @lc code=end

