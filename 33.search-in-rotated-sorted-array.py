#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[low] < nums[mid]:
                low = mid
            else:
                high = mid

        k = low + 1
        unrotated = nums[k:] + nums[:k]
        found = bisect_left(unrotated, target)

        if found == len(unrotated) or unrotated[found] != target:
            return -1
        
        return (found + k) % len(nums)

# @lc code=end

