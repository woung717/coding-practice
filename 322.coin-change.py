#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = dict()

        def dfs(remain: int) -> int:
            if remain == 0:
                return 0
            
            if remain < 0:
                return -1

            if remain in dp:
                return dp[remain]
            
            min_n = 10**4
            for d in coins:
                n = dfs(remain - d)
                if n != -1:
                    min_n = min(min_n, n)

            dp[remain] = min_n + 1 if min_n != 10**4 else -1

            return dp[remain]
        

        return dfs(amount)

        
# @lc code=end

