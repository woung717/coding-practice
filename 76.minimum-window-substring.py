#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        if s == t:
            return s
        
        candidate = (0, float('inf'))

        need = Counter(t)
        need_len = len(need)

        got = defaultdict(int)
        got_len = 0

        tail = 0
        for head, ch in enumerate(s):
            if ch not in need:
                continue

            got[ch] += 1
            if got[ch] == need[ch]:
                got_len += 1

            while need_len == got_len:
                if head - tail < candidate[1] - candidate[0]:
                    candidate = (tail, head)

                ct = s[tail]
                if ct in need:
                    got[ct] -= 1
                    if got[ct] < need[ct]:
                        got_len -=1

                tail += 1

        if candidate[1] - candidate[0] == float('inf'):
            return ""
        
        return s[candidate[0]: candidate[1] + 1]

        
# @lc code=end

