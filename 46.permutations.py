#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (78.08%)
# Likes:    18659
# Dislikes: 317
# Total Accepted:    2M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#

# @lc code=start
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def recursive(permutation: list, candidate_nums: list):
            if len(permutation) == len(nums):
                ret.append(permutation)
                return
            
            for i, c in enumerate(candidate_nums):
                recursive(permutation + [c], candidate_nums[:i] + candidate_nums[i + 1:])
        
        recursive([], nums)

        return ret
                
        # return permutations(nums, len(nums))
# @lc code=end

