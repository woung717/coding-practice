#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (63.65%)
# Likes:    8166
# Dislikes: 832
# Total Accepted:    864.8K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
# 
# You are also given three integers sr, sc, and color. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
# 
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with color.
# 
# Return the modified image after performing the flood fill.
# 
# 
# Example 1:
# 
# 
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
# 
# 
# Example 2:
# 
# 
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made
# to the image.
# 
# 
# 
# Constraints:
# 
# 
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n
# 
# 
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        OFFSETS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        done = set()
        starting_color = image[sr][sc]
        queue = [(sr, sc)]

        while len(queue):
            r, c = queue.pop(0)

            for offset in OFFSETS:
                next_r, next_c = r + offset[0], c + offset[1]

                if 0 <= next_r < len(image) and 0 <= next_c < len(image[0]) and \
                    (next_r, next_c) not in done and \
                    image[next_r][next_c] == starting_color: 
                    queue.append((next_r, next_c))

            image[r][c] = color
            done.add((r, c))

        return image
            
        
# @lc code=end

