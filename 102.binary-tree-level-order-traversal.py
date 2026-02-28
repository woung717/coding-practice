#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        nodes_by_level = defaultdict(list)

        def dfs(root: Optional[TreeNode], depth: int, node_dict: dict):
            if root is None:
                return
            
            node_dict[depth].append(root.val)

            dfs(root.left, depth + 1, node_dict)
            dfs(root.right, depth + 1, node_dict)

        
        dfs(root, 0, nodes_by_level)
        
        ret = []
        for depth in range(len(nodes_by_level)):
            ret.append(nodes_by_level[depth])

        return ret

        
# @lc code=end

