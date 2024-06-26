#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (44.14%)
# Likes:    16740
# Dislikes: 260
# Total Accepted:    850.9K
# Total Submissions: 1.9M
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
# 
# 
# Example 1:
# 
# 
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
# 
# 
# Example 2:
# 
# 
# Input: heights = [2,4]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while len(stack) > 0 and stack[-1][1] >= h:
                popped_i, popped_h = stack.pop()
                max_area = max(max_area, (i - popped_i) * popped_h)
                start = popped_i
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area
                           

# @lc code=end

