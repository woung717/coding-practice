#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from collections import Counter

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         color_count = Counter(nums)

#         i = 0
#         for n in (0, 1, 2):
#             if n not in color_count:
#                 continue
            
#             for _ in range(color_count[n]):
#                 nums[i] = n
#                 i += 1

#         return nums

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        def swap(nums: List[int], i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]

        while mid <= high:
            match nums[mid]:
                case 0:
                    swap(nums, low, mid)
                    low += 1
                    mid += 1
                case 1:
                    mid += 1
                case 2:
                    swap(nums, mid, high)
                    high -=1

        return nums

# @lc code=end

