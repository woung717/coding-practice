#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10**4
        max_profit = 0

        for p in prices:
            profit = p - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, p)

        return max_profit 
        
# @lc code=end

