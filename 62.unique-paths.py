#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (64.14%)
# Likes:    16310
# Dislikes: 432
# Total Accepted:    1.8M
# Total Submissions: 2.7M
# Testcase Example:  '3\n7'
#
# There is a robot on an m x n grid. The robot is initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
# 
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
# 
# The test cases are generated so that the answer will be less than or equal to
# 2 * 10^9.
# 
# 
# Example 1:
# 
# 
# Input: m = 3, n = 7
# Output: 28
# 
# 
# Example 2:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        queue = deque([(m, n)])
        ways_dict = defaultdict(int)
        ways_dict[(m, n)] = 1
        seen = set()

        while queue:
            i, j = queue.popleft()

            next_i = i - 1
            if next_i >= 1 and (next_i, j) not in seen:
                queue.append((next_i, j))
                seen.add((next_i, j))
                
            next_j = j - 1
            if next_j >= 1 and (i, next_j) not in seen:
                queue.append((i, next_j))
                seen.add((i, next_j))
            
            ways_dict[(i, j)] += ways_dict[(i + 1, j)] + ways_dict[(i, j + 1)]
        
        return ways_dict[(1, 1)]


# @lc code=end

