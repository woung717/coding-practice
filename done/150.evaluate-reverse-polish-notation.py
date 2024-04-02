#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (51.03%)
# Likes:    7444
# Dislikes: 1052
# Total Accepted:    994.5K
# Total Submissions: 1.9M
# Testcase Example:  '["2","1","+","3","*"]'
#
# You are given an array of strings tokens that represents an arithmetic
# expression in a Reverse Polish Notation.
# 
# Evaluate the expression. Return an integer that represents the value of the
# expression.
# 
# Note that:
# 
# 
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish
# notation.
# The answer and all the intermediate calculations can be represented in a
# 32-bit integer.
# 
# 
# 
# Example 1:
# 
# 
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# 
# Example 2:
# 
# 
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# 
# 
# Example 3:
# 
# 
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
# 
# 
#

# @lc code=start
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []

#         for t in tokens:
#             if t in {"+", "-", "*", "/"}:
#                 right, left = stack.pop(), stack.pop()
#                 stack.append(str(int(eval(left + t + right))))
#             else:
#                 stack.append(t)

#         return int(stack.pop())

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(left: str, op: str, right: str) -> str:
            left, right = int(left), int(right)
            ret = 0

            if op == "+": ret = left + right
            elif op == "-": ret = left - right
            elif op == "*": ret = left * right
            elif op == "/": ret = int(left / right)
            else: ret = None

            return str(ret)
        
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                right, left = stack.pop(), stack.pop()
                stack.append(calc(left, t, right))
            else:
                stack.append(t)

        return int(stack.pop())
        
# @lc code=end

