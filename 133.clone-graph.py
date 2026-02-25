#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# from typing import Optional
# from collections import deque

# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if node is None:
#             return None
        
#         new_nodes = dict()
#         queue = deque()

#         new_nodes[node.val] = Node(node.val, [])
#         queue.append(node)
#         while len(queue) > 0:
#             current_node = queue.popleft()
            
#             for next_node in current_node.neighbors:
#                 if next_node.val not in new_nodes:
#                     new_nodes[next_node.val] = Node(next_node.val, [])
#                     queue.append(next_node)

#                 new_nodes[current_node.val].neighbors.append(new_nodes[next_node.val])

#         return new_nodes[node.val]
                    
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        new_nodes = dict()
        queue = deque()

        new_nodes[node.val] = Node(node.val)
        queue.append(node)

        while len(queue) > 0:
            current_node = queue.popleft()

            for next_node in current_node.neighbors:
                if next_node.val not in new_nodes:
                    new_nodes[next_node.val] = Node(next_node.val)
                    queue.append(next_node)
                
                new_nodes[current_node.val].neighbors.append(new_nodes[next_node.val])

        return new_nodes[node.val]
        
# @lc code=end

