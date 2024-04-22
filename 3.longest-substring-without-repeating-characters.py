#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.57%)
# Likes:    38829
# Dislikes: 1814
# Total Accepted:    5.5M
# Total Submissions: 16M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs_set = set()
        left = 0
        ret = 0

        for right, c in enumerate(s):
            while c in subs_set:
                subs_set.remove(s[left])
                left += 1
            
            subs_set.add(c)
            ret = max(ret, right - left + 1)
        
        return ret


                
# @lc code=end

