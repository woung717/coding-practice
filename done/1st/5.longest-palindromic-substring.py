#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (33.67%)
# Likes:    28715
# Dislikes: 1718
# Total Accepted:    2.9M
# Total Submissions: 8.7M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def get_palindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]
        
        ret = ""
        for i in range(len(s)):
            odd = get_palindrome(i, i)
            even = get_palindrome(i, i + 1)

            palindrome = max(odd, even, key= lambda x: len(x))
            ret = max(ret, palindrome, key= lambda x: len(x))

        return ret

# @lc code=end

