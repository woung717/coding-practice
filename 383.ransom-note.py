#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start

from collections import Counter

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ransom_note_c_counter = Counter(ransomNote)

#         for c in magazine:
#             if c in ransom_note_c_counter:
#                 ransom_note_c_counter[c] -= 1

#         for count in ransom_note_c_counter.values():
#             if count > 0:
#                 return False
            
#         return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        
        return True
# @lc code=end

