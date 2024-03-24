#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (46.64%)
# Likes:    16869
# Dislikes: 759
# Total Accepted:    1.6M
# Total Submissions: 3.5M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:            
        word_set = set(wordDict)
        fails = set()

        def recurse(s, i):
            if s == "":
                return True
            
            if i > len(s) or s in fails:
                fails.add(s)
                return False

            ret = False
            if s[:i] in word_set:
                ret |= recurse(s[i:], 0)
            
            return ret or recurse(s, i + 1)

        return recurse(s, 0)

# @lc code=end

