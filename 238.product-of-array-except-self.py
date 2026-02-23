#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1 for _ in range(len(nums))]

        tmp = 1
        for i in range(1, len(nums)):
            tmp *= nums[i - 1]
            ret[i] *= tmp

        tmp = 1
        for j in range(len(nums) - 2, -1, -1):
            tmp *= nums[j + 1]
            ret[j] *= tmp

        return ret


# @lc code=end

