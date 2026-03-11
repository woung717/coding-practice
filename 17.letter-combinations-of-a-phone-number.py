#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            2: "abc", 3: "def", 4: "ghi",
            5: "jkl", 6: "mno", 7: "pqrs",
            8: "tuv", 9: "wxyz"
        }

        def recurse(remain_digits: str, path: str):
            if remain_digits == "":
                return [path]
            
            ret = []
            for c in letter_dict[int(remain_digits[0])]:
                for p in recurse(remain_digits[1:], path + c):
                    ret.append(p)

            return ret
        
        return recurse(digits, "")
            
            
        
# @lc code=end

