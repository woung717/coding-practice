#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (53.31%)
# Likes:    9211
# Dislikes: 942
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
# 
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return "{0:b}".format(int(a, 2) + int(b, 2))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_n = 0
        for c in a:
            a_n <<= 1
            a_n |= 1 if c == '1' else 0

        b_n = 0
        for c in b:
            b_n <<= 1
            b_n |= 1 if c == '1' else 0

        ret = ""
        n = a_n + b_n
        while n:
            ret = ('1' if n & 1 else '0') + ret
            n >>= 1
        
        return ret if len(ret) else "0"
    
# @lc code=end

