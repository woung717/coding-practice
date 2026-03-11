#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def recurse(i: int, path: list):
            if i == len(nums):
                return [path]
            
            ret = []
            ret += [p for p in recurse(i + 1, path)]
            ret += [p for p in recurse(i + 1, path[:] + [nums[i]])]

            return ret


        return recurse(0, [])
            
        
# @lc code=end

