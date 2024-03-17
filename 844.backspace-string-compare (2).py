#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (49.11%)
# Likes:    7430
# Dislikes: 347
# Total Accepted:    802.5K
# Total Submissions: 1.6M
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
# 
# Note that after backspacing an empty text, the text will continue empty.
# 
# 
# Example 1:
# 
# 
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# 
# 
# Example 2:
# 
# 
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# 
# 
# Example 3:
# 
# 
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
# 
# 
# 
# Follow up: Can you solve it in O(n) time and O(1) space?
# 
#

# @lc code=start
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def render(s: str) -> str:
#             stack = []

#             for c in s:
#                 if c == '#':
#                     if len(stack): stack.pop()
#                 else:
#                     stack.append(c)

#             return "".join(stack)

#         return render(s) == render(t)

import re

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def render(s: str) -> str:
            regex = re.compile(r"[a-z]{1}#")

            for _ in range(len(s)):
                s = regex.sub('', s)

            return s.replace('#', '')
        
        return render(s) == render(t)
        
# @lc code=end

