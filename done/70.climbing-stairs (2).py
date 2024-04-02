#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()

        def climb(m):
            if m <= 2: return m
            if m in memo: return memo[m]

            memo[m] = climb(m - 1) + climb(m - 2)
             
            return memo[m]
        
        return climb(n)

        
# @lc code=end
