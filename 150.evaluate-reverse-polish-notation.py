#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from math import trunc
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calc(x: int, y: int, op: str) -> int:
            match op:
                case "+":
                    return x + y
                case "-":
                    return x - y
                case "*":
                    return x * y
                case "/":
                    return trunc(x / y)

        for c in tokens:
            if c.replace("-", "").isdigit():
                stack.append(int(c))
            else:
                y = stack.pop()
                x = stack.pop()
                result = calc(x, y, c)

                stack.append(result)
        
        return stack[0]
        
# @lc code=end

