#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start

from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found_index = bisect_left(nums, target)

        if found_index == len(nums) or \
            nums[found_index] != target:
            found_index = -1

        return found_index
# @lc code=end

