#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        ret = 0
        tail = 0
        chars_dict = dict()

        for head, c in enumerate(s):
            if c in chars_dict:
                tail = max(tail, chars_dict[c] + 1)

            chars_dict[c] = head
            ret = max(ret, head - tail + 1)
        
        return ret

# @lc code=end

