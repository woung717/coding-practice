#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        ret_l, ret_r = 0, 0

        def longest_palindrome(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l + 1, r - 1

        for i in range(len(s)):
            l_odd, r_odd = longest_palindrome(i, i)
            
            if r_odd - l_odd > ret_r - ret_l:
                ret_l, ret_r = l_odd, r_odd

            l_even, r_even = longest_palindrome(i, i + 1)

            if r_even - l_even > ret_r - ret_l:
                ret_l, ret_r = l_even, r_even

        
        return s[ret_l:ret_r + 1]
        

# @lc code=end

