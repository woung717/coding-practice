#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            stack.append(c)

            if len(stack) >=2 and \
                (stack[-2] + stack[-1]) in ('()', '[]', '{}'):
                stack.pop()
                stack.pop()

        return len(stack) == 0


        
# @lc code=end

