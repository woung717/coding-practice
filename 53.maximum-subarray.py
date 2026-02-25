#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]
        sub_sum = nums[0]

        for i in range(1, len(nums)):
            if sub_sum < 0:
                sub_sum = 0

            sub_sum += nums[i]
            ret = max(ret, sub_sum)

        return ret
    
# @lc code=end

