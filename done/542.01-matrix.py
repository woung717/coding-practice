#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (48.21%)
# Likes:    9222
# Dislikes: 408
# Total Accepted:    537.6K
# Total Submissions: 1.1M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        done = set()
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    done.add((i, j))

        while len(queue) > 0:
            i_q, j_q = queue.popleft()
            for o in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                next_i, next_j = i_q + o[0], j_q + o[1]
                if 0 <= next_i < m and 0 <= next_j < n and \
                    (next_i, next_j) not in done:
                    mat[next_i][next_j] = mat[i_q][j_q] + 1
                    queue.append((next_i, next_j))
                    done.add((next_i, next_j))
                            
        return mat
        
# @lc code=end

