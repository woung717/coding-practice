#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start

from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if  len(s) < len(p):
            return []
        
        ret = []
        p_counter = Counter(p)
        window_counter = defaultdict(int)

        for i, c in enumerate(s):
            window_counter[c] += 1

            if i >= len(p):
                out = s[i - len(p)]
                window_counter[out] -= 1
                if window_counter[out] == 0:
                    del window_counter[out]

            if p_counter == window_counter:
                ret.append(i - (len(p) - 1))


        return ret
        
# @lc code=end

