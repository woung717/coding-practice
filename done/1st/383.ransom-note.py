#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (60.95%)
# Likes:    4833
# Dislikes: 492
# Total Accepted:    1.1M
# Total Submissions: 1.8M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for key in ransomNote_counter.keys():
            if ransomNote_counter[key] > magazine_counter[key]:
                return False
            
        return True
        
# @lc code=end

