#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (68.35%)
# Likes:    18796
# Dislikes: 595
# Total Accepted:    2.8M
# Total Submissions: 4M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         str_dict = defaultdict(list)
#         alphabets = [chr(c) for c in range(ord('a'), ord('z') + 1)]

#         for s in strs:
#             str_counter = Counter(s)
#             encoding = ''
#             for a in alphabets:
#                 if a in str_counter:
#                     encoding = encoding + a + str(str_counter[a])
#             str_dict[encoding].append(s)
        
#         return str_dict.values()
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for s in strs:
            anagram_dict[tuple(sorted(s))].append(s)
        
        return anagram_dict.values()



# @lc code=end

