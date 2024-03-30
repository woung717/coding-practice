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
        s = '(' + s.replace(" ", "") + ')'
        stack = []

        for c in s:
            if c.isdigit() or c in ('+', '-', '('):
                stack.append(c)
            elif c == ')':
                temp = ')'

                while temp[0] != '(':
                    temp = stack.pop() + temp
                
                op = 1
                answer = 0
                number = ''
                for c2 in temp[1:]:
                    if c2.isdigit():
                        number += c2
                    elif c2 in ('+', '-'):
                        if number:
                            answer += int(number) * op
                            number = ''
                            op = 1
                        op *= 1 if c2 == '+' else -1 

                answer += int(number) * op

                stack.append(str(answer))
        
        return int(stack.pop())
# @lc code=end

