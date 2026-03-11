#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start

# from collections import deque

# class Solution:
#     def get_max_depth(self, adj_list: List[List[int]], start_node: int):
#         max_depth = 0

#         visited = set()
#         queue = deque()

#         visited.add(start_node)
#         queue.append((start_node, 0))

#         while len(queue) > 0:
#             curr_node, depth = queue.popleft()

#             max_depth = max(max_depth, depth)

#             for next_node in adj_list[curr_node]:
#                 if next_node not in visited:
#                     visited.add(next_node)
#                     queue.append((next_node, depth + 1))

#         return max_depth

#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if len(edges) == 0:
#             return [0]
        
#         adj_list = [[] for _ in range(n)]

#         for a, b in edges:
#             adj_list[a].append(b)
#             adj_list[b].append(a)

#         depths = []
#         for root in range(len(adj_list)):
#             depth = self.get_max_depth(adj_list, root)
#             depths.append((depth, root))

#         depths.sort()

#         return [node for depth, node in depths if depth == depths[0][0]]
    
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        
        adj_list = [set() for _ in range(n)]

        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        connected_nodes = { i for i in range(n) }
        queue = deque()
        for i, nexts in enumerate(adj_list):
            if len(nexts) == 1:
                queue.append(i)

        while len(connected_nodes) > 2:
            visited = set()
            next_queue = deque()
            while len(queue) > 0:
                curr_node = queue.popleft()

                for next_node in adj_list[curr_node]:
                    if next_node not in visited:
                        adj_list[next_node].remove(curr_node)

                        if len(adj_list[next_node]) == 1:
                            visited.add(next_node)
                            next_queue.append(next_node)

                adj_list[curr_node].clear()
                connected_nodes.remove(curr_node)
            
            queue = next_queue

        return list(connected_nodes)

# @lc code=end

