#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        non_space = s.replace(' ', '')

        if non_space == '':
            return 0
        
        non_space = '(' + non_space + ')'

        def simple_calc(stack: list[str]):
            statement = []
            while len(stack) > 0:
                e = stack.pop()
                if e == '(':
                    break
                statement.append(e)
            
            statement = statement[::-1]

            result = 0
            if statement[0] != '-':
                statement = ['+'] + statement

            for i in range(0, len(statement), 2):
                sign = -1 if statement[i] == '-' else 1
                result += sign * int(statement[i + 1])
            
            stack.append(str(result))

        stack = []
        num = ''
        for c in non_space:
            if c == '(':
                stack.append('(')
            elif c == ')':
                if num != '':
                    stack.append(num)
                    num = ''
                simple_calc(stack)
            elif c.isnumeric():
                num += c
            elif c in ('+', '-'):
                if num != '':
                    stack.append(num)
                    num = ''
                stack.append(c)

        if len(stack) > 1:
            simple_calc(stack)

        return int(stack[0])

# @lc code=end

