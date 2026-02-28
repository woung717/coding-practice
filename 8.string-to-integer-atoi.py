#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        is_positive = True
        has_effective = False
        cleaned = ""

        for c in s:
            if has_effective and c in ('+', '-', ' '):
                break
            elif c == ' ':
                continue
            elif c.isdigit():
                has_effective = True
                cleaned += c
            elif c in ('+', '-'):
                has_effective = True
                is_positive = c == '+'
            else:
                break

        non_leading_0 = ""
        for c in cleaned:
            if non_leading_0 == "" and c == '0':
                continue
            non_leading_0 += c

        if non_leading_0 == "":
            return 0
        
        float_number = float(non_leading_0) * (-1 if not is_positive else 1)
        float_number = min(2**31 - 1, float_number)
        float_number = max(-2**31, float_number)

        return int(float_number)
        
# @lc code=end

