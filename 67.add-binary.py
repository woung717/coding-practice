#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def atob(s: str) -> int:
            ret = 0
            for c in s:
                ret <<= 1
                if c == '1':
                    ret |= 1
            
            return ret
        
        def btoa(b: int) -> str:
            ret = ''

            while b:
                ret = ('1' if b & 1 else '0') + ret
                b >>= 1

            return ret if ret else '0'

        ret_b = atob(a) + atob(b)

        return btoa(ret_b)

                
            
        
# @lc code=end

