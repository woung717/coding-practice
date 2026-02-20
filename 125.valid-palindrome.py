#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i].isalnum() and s[j].isalnum() and \
                s[i].lower() != s[j].lower():
                return False

            if not s[j].isalnum():
                j -= 1
            elif not s[i].isalnum():
                i += 1
            else:
                i += 1
                j -= 1
            
        return True

        
# @lc code=end

