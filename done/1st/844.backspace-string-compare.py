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
# Total Accepted:    802.6K
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
#         s_pointer, t_pointer = len(s) - 1, len(t) - 1
#         s_skip, t_skip = 0, 0

#         while s_pointer >= 0 or t_pointer >= 0:
#             while s_pointer >= 0:
#                 if s[s_pointer] == "#":
#                     s_skip += 1
#                 elif s_skip > 0:
#                     s_skip -= 1
#                 else:
#                     break
#                 s_pointer -= 1
            
#             while t_pointer >= 0:
#                 if t[t_pointer] == "#":
#                     t_skip += 1
#                 elif t_skip > 0:
#                     t_skip -= 1
#                 else:
#                     break
#                 t_pointer -= 1
            
#             if s_pointer >= 0 and t_pointer >= 0 and s[s_pointer] != t[t_pointer]:
#                 return False
            
#             if (s_pointer >= 0) != (t_pointer >= 0):
#                 return False

#             s_pointer -= 1
#             t_pointer -= 1
        
#         return True

from itertools import zip_longest

class Solution(object):
    def backspaceCompare(self, s, t):
        def step(backspace_string):
            skip = 0
            for c in backspace_string[::-1]:
                if c == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield c

        for s_c, t_c in zip_longest(step(s), step(t)):
            if s_c != t_c: return False

        return True


# @lc code=end

