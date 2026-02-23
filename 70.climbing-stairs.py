#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 2}

        def recurse(n: int):
            if n in dp:
                return dp[n]
            
            dp[n] = recurse(n - 1) + recurse(n - 2)

            return dp[n]

        return recurse(n)

        
# @lc code=end

1
- 1

2
- 1 1
- 2

3
- 1 1 1
- 1 2
- 2 1

4
- 1 1 1 1
- 1 2 1
- 2 1 1
- 1 1 2
- 2 2

5
- 1 1 1 1 1
- 1 2 1 1 

- 1 2 1 2
- 2 1 1 1 1
- 2 1 1 2
- 