#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (58.59%)
# Likes:    22056
# Dislikes: 486
# Total Accepted:    2.5M
# Total Submissions: 4.3M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ret = 0
        queue = deque()

        def fill(i, j):
            grid[i][j] = '0'
            queue.append((i, j))

            while queue:
                k, l = queue.popleft()

                for o in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    m, n = k + o[0], l + o[1]
                    if 0 <= m < len(grid) and \
                        0 <= n < len(grid[0]) and \
                        grid[m][n] == '1':
                        grid[m][n] = '0'
                        queue.append((m, n))

        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == '1':
                    fill(a, b)
                    ret += 1
        
        return ret


# @lc code=end

