#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        encoded = list()

        def traverse(root: TreeNode):
            if root is None:
                encoded.append('n')
                return
            
            encoded.append(str(root.val))

            traverse(root.left)
            traverse(root.right)

        traverse(root)

        return ','.join(encoded)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_list = data.split(',')

        def make_tree(str_list: List[str]) -> TreeNode:
            if len(str_list) == 0:
                return None
            
            s = str_list.pop()

            if s == 'n':
                return None
            
            node = TreeNode(int(s))

            node.left = make_tree(str_list)
            node.right = make_tree(str_list)

            return node
        
        return make_tree(node_list[::-1])

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

