#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            remain = target - n

            remain_index = indices.get(remain, None)
            if remain_index and remain_index != i:
                return [i, remain_index]
        
# @lc code=end

