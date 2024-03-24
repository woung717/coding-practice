#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (49.03%)
# Likes:    14362
# Dislikes: 1263
# Total Accepted:    1.4M
# Total Submissions: 2.8M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        MAX = len(matrix) * len(matrix[0])
        phase = False   # False is column scan / True is row scan 
        col_direction, row_direction = 1, 1
        col, row = 0, 0
        done = set()
        ret = []

        while len(ret) != MAX:
            ret.append(matrix[row][col])
            done.add((col, row))

            if phase == False:
                next_col = col + col_direction 
                if 0 <= next_col < len(matrix[0]) and (next_col, row) not in done:
                    col = next_col
                else:
                    phase = not phase
                    col_direction *= -1
                    row += row_direction
            else:
                next_row = row + row_direction
                if 0 <= next_row < len(matrix) and (col, next_row) not in done:
                    row = next_row
                else:
                    phase = not phase
                    row_direction *= -1
                    col += col_direction
        
        return ret

# @lc code=end

