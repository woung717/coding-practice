#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (42.82%)
# Likes:    17520
# Dislikes: 711
# Total Accepted:    1.3M
# Total Submissions: 3.1M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty
# string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# 
# Example 2:
# 
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
# 
# Constraints:
# 
# 
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
# 
#

# @lc code=start
from collections import Counter, defaultdict
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_dict = defaultdict(lambda: 0)
        needed_dict = Counter(t)
        needed_alphabets = len(t)

        head = 0
        min_head, min_tail = 0, math.inf

        for tail in range(len(s)):
            added = s[tail]

            if added in needed_dict:
                window_dict[added] += 1
                if window_dict[added] <= needed_dict[added]:
                    needed_alphabets -= 1
            
            while needed_alphabets == 0 and head <= tail:
                if tail - head < min_tail - min_head:
                    min_tail, min_head = tail, head

                popped = s[head]
                if popped in needed_dict:
                    window_dict[popped] -= 1
                    if window_dict[popped] < needed_dict[popped]:
                        needed_alphabets += 1
                head += 1
                
        return "" if min_tail == math.inf else s[min_head: min_tail + 1]


# @lc code=end

