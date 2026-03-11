#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        left, right = 0, len(height) - 1

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            ret = max(ret, width * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ret
        
# @lc code=end

