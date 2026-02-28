#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
# from collections import deque

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ret = 0
#         queue = deque()
#         visited = set()

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     queue.append((i, j))
#                     visited.add((i, j))

#                     while len(queue) > 0:
#                         r, c = queue.popleft()

#                         for o_r, o_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#                             if 0 <= r + o_r < len(grid) and \
#                                 0 <= c + o_c < len(grid[0]) and \
#                                 grid[r + o_r][c + o_c] == "1" and \
#                                 (r + o_r, c + o_c) not in visited:
#                                 visited.add((r + o_r, c + o_c))
#                                 queue.append((r + o_r, c + o_c))

#                     ret += 1

#         return ret

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        queue = deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    queue.append((i, j))
                    grid[i][j] = "0"

                    while len(queue) > 0:
                        r, c = queue.popleft()

                        for o_r, o_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            if 0 <= r + o_r < len(grid) and \
                                0 <= c + o_c < len(grid[0]) and \
                                grid[r + o_r][c + o_c] == "1":
                                queue.append((r + o_r, c + o_c))
                                grid[r + o_r][c + o_c] = "0"

                    ret += 1

        return ret

        
# @lc code=end

