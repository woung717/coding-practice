
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start

class Solution:
    def __init__(self) -> None:
        self.dp = dict()

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        
        if (m, n) in self.dp:
            return self.dp[(m, n)]
        
        if m == 1 and n == 1:
            return 1

        ret = 0
        ret += self.uniquePaths(m - 1, n)
        ret += self.uniquePaths(m, n - 1)

        self.dp[(m, n)] = ret

        return ret
# @lc code=end

