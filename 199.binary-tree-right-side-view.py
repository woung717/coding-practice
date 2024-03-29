#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (62.87%)
# Likes:    11707
# Dislikes: 892
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root = [1,null,3]
# Output: [1,3]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, 0)])
        level_nodes = defaultdict(list)
        max_level = -1

        while queue:
            node, level = queue.popleft()
            
            if node is None:
                continue

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

            max_level = max(max_level, level)
            level_nodes[level].append(node.val)
        
        return [level_nodes[i][-1] for i in range(max_level + 1)]
            
# @lc code=end

