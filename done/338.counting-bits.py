#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (78.09%)
# Likes:    10889
# Dislikes: 518
# Total Accepted:    1.1M
# Total Submissions: 1.4M
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# 
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 0 --> 0 0
# 1 --> 1 1 2^0
# 2 --> 10 1 2^1
# 3 --> 11 2
# 4 --> 100 1 2^2
# 5 --> 101 2
# 6 --> 110 2
# 7 --> 111 3
# 8 --> 1000 1 2^3
# 9 --> 1001 2
# 10 --> 1010 2
# 11 --> 1011 3
# 12 --> 1100 2
# 13 --> 1101 3
# 14 --> 1110 3
# 15 --> 1111 4

# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^5
# 
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
# 
# 
#

# @lc code=start

import math

class Solution:
    def countBits(self, n: int) -> List[int]:
        count_dict = { 0: 0 }

        def count(n):
            if n == 0: return 0
            
            remain = n - 2**int(math.log2(n))
            count_dict[n] = count_dict[remain] + 1

            return count_dict[n]
        
        return [count(i) for i in range(n + 1)]
        
# @lc code=end

