#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (34.25%)
# Likes:    30054
# Dislikes: 2756
# Total Accepted:    3.4M
# Total Submissions: 9.8M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
# from itertools import combinations

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ret = set()

#         for n3 in combinations(sorted(nums), 3):
#             if n3[0] + n3[1] + n3[2] == 0 and (n3[0], n3[1], n3[2]) not in ret:
#                 ret.add((n3[0], n3[1], n3[2]))

#         return ret

from bisect import bisect_right

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        index_dict = { n: i for i, n in enumerate(nums) }

        for n in range(len(nums) - 2):
            for m in range(n + 1, len(nums) - 1):
                remain = -(nums[n] + nums[m])
                if remain < nums[m]: break
                if remain in index_dict and index_dict[remain] not in (n, m):
                    index = index_dict[remain]
                    if remain >= nums[m]: 
                        ret.add((nums[n], nums[m], nums[index]))
                    elif remain <= nums[n]:
                        ret.add((nums[index], nums[n], nums[m]))
                    else:
                        ret.add((nums[n], nums[index], nums[m]))
                        
        return ret

# @lc code=end

