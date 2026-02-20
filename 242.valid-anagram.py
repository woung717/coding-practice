#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for c, n in s_counter.items():
            if t_counter[c] != n:
                return False

        for c, n in t_counter.items():
            if s_counter[c] != n:
                return False
            
        return True
        
# @lc code=end

