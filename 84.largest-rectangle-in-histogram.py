#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         ret = 0
#         stack = [-1]

#         for i, h in enumerate(heights + [0]):
#             while len(stack) > 1 and h < heights[stack[-1]]:
#                 prev_height_index = stack.pop()
#                 space = (i - stack[-1] - 1) * heights[prev_height_index]
#                 ret = max(ret, space)

#             stack.append(i)

#         return ret

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        stack = [-1]

        for i, h in enumerate(heights + [0]):
            while len(stack) > 1 and h < heights[stack[-1]]:
                prev_bar_i = stack.pop()
                width = i - stack[-1] - 1
                height = heights[prev_bar_i]
                ret = max(ret, width * height)

            stack.append(i)

        return ret

        
# @lc code=end

