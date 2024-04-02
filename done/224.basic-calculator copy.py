#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (43.27%)
# Likes:    6170
# Dislikes: 475
# Total Accepted:    452.1K
# Total Submissions: 1M
# Testcase Example:  '"1 + 1"'
#
# Given a string s representing a valid expression, implement a basic
# calculator to evaluate it, and return the result of the evaluation.
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
# 
# 
# Example 1:
# 
# 
# Input: s = "1 + 1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: s = " 2-1 + 2 "
# Output: 3
# 
# 
# Example 3:
# 
# 
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is
# invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is
# valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        ret = 0
        i, sign_stack = 0, [1, 1]

        while i < len(s):
            c = s[i]

            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                ret += sign_stack.pop() * int(s[start:i])
                continue
            elif c in "+-(":
                sign_stack.append(sign_stack[-1] * (-1 if c == '-' else 1))
            elif c == ')':
                sign_stack.pop()
            i += 1

        return ret
# @lc code=end

