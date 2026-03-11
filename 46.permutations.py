#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def recurse(choosed: list, used: set, ret: list):
            if len(choosed) == len(nums):
                ret.append(choosed[:])
                return
            
            for i in range(len(nums)):
                if i not in used:
                    choosed.append(nums[i])
                    used.add(i)
                    recurse(choosed, used, ret)
                    choosed.pop()
                    used.remove(i)

        ret = []

        recurse([], set(), ret)

        return ret


        
# @lc code=end

