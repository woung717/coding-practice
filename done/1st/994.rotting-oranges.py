#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (53.90%)
# Likes:    12382
# Dislikes: 388
# Total Accepted:    797.4K
# Total Submissions: 1.5M
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
# 
# 
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# Example 3:
# 
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshes, rottens = set(), deque()
        ret = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: freshes.add((i, j))
                elif grid[i][j] == 2: rottens.append((i, j))
        
        while freshes and rottens:
            for _ in range(len(rottens)):
                k, l = rottens.popleft()

                for o in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    m, n = k + o[0], l + o[1]

                    if (m, n) in freshes:
                        freshes.remove((m, n))
                        rottens.append((m, n))
            ret += 1
        
        return ret if not freshes else -1
    
# @lc code=end

