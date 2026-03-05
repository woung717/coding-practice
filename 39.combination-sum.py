#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = list()
        candidates.sort()

        def recurse(remain: int, start: int, used: list):
            if remain < 0:
                return
            
            if remain == 0:
                ret.append(used[:])

            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break

                used.append(candidates[i])
                recurse(remain - candidates[i], i, used)
                used.pop()

        recurse(target, 0, [])

        return ret

                
# @lc code=end

