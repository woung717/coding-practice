#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        nodes_by_level = list()
        queue = deque()
        queue.append((root, 0))

        while len(queue) > 0:
            node, level = queue.popleft()

            if len(nodes_by_level) - 1 < level:
                nodes_by_level.append([])

            nodes_by_level[level].append(node.val)

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

        return [l[-1] for l in nodes_by_level]

        
# @lc code=end

