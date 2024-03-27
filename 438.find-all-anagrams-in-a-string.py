#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (50.81%)
# Likes:    12171
# Dislikes: 336
# Total Accepted:    856.2K
# Total Submissions: 1.7M
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# 
# 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# Example 2:
# 
# 
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
# 
# 
#

# @lc code=start

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_length = len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])
        
        ret = []
        for i in range(len(s) - len(p) + 1):
            if i != 0:
                s_counter[s[i - 1]] -= 1
                if s[i + p_length - 1] in s_counter:
                    s_counter[s[i + p_length - 1]] += 1
                else:
                    s_counter[s[i + p_length - 1]] = 1

            if p_counter == s_counter:
                ret.append(i)
        
        return ret
            
# @lc code=end

