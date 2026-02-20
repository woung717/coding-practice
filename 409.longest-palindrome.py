#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = False
        longest = 0

        for n in Counter(s).values():
            if n % 2: 
                odd = True

            longest += n // 2

        return 2 * longest + odd
            
# @lc code=end

