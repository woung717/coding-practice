#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (56.58%)
# Likes:    9931
# Dislikes: 374
# Total Accepted:    848.2K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# 
# 
# Example 2:
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
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def __init__(self):
        self.NULL = "null"
        self.delimiter = ","

    def serialize(self, root):
        preorder = []

        def _preorder(node):
            if node is None:
                preorder.append(self.NULL)
            else:
                preorder.append(str(node.val))
                _preorder(node.left)
                _preorder(node.right)

        _preorder(root)

        return self.delimiter.join(preorder)
        

    def deserialize(self, data):
        if len(data) == 0: 
            return None
        
        queue = deque(data.split(self.delimiter))

        def build_tree():
            val = queue.popleft()

            if val == self.NULL:
                return None
            
            node = TreeNode(int(val))
            node.left, node.right  = build_tree(), build_tree()

            return node
        
        return build_tree()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

