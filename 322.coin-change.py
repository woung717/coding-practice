#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (43.67%)
# Likes:    18519
# Dislikes: 433
# Total Accepted:    1.7M
# Total Submissions: 3.9M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def decrease(remain):
            if remain == 0: return 0
            if remain < 0: return math.inf
            if remain in memo: return memo[remain]
            
            memo[remain] = min([decrease(remain - d) + 1 for d in coins])

            return memo[remain]
        
        ret = decrease(amount)
        
        return ret if ret != math.inf else -1 


# @lc code=end

