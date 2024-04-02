#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_p_index = max_p_index = 0

        while max_p_index < len(prices):
            if prices[max_p_index] > prices[min_p_index]:
                profit = prices[max_p_index] - prices[min_p_index]
                max_profit = max(max_profit, profit)
            else:
                min_p_index = max_p_index

            max_p_index += 1

        return max_profit
            



        
# @lc code=end

