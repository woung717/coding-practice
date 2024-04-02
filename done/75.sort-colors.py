#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (61.81%)
# Likes:    17650
# Dislikes: 618
# Total Accepted:    1.8M
# Total Submissions: 3M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in
# the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and
# blue, respectively.
# 
# You must solve this problem without using the library's sort function.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,0,1]
# Output: [0,1,2]
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# 
# 
# 
# Follow up: Could you come up with a one-pass algorithm using only constant
# extra space?
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red_pointer, white_pointer, blue_pointer = 0, 0, len(nums) - 1

        while white_pointer <= blue_pointer:
            if nums[white_pointer] == 0:
                nums[red_pointer], nums[white_pointer] = nums[white_pointer], nums[red_pointer]
                red_pointer += 1
                white_pointer += 1
            elif nums[white_pointer] == 1:
                white_pointer += 1
            else:
                nums[blue_pointer], nums[white_pointer] = nums[white_pointer], nums[blue_pointer]
                blue_pointer -= 1
        
# @lc code=end

