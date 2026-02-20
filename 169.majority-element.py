#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start

from collections import defaultdict

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count_list = defaultdict(lambda: 0)

#         for n in nums:
#             count_list[n] += 1

#         acc = 0
#         for n, count in count_list.items():
#             acc += count

#             if acc >= (len(nums) + 1) // 2:
#                 return n
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = majority = 0

        for n in nums:
            if count == 0:
                majority = n

            count += 1 if n == majority else -1
        
        return majority

# @lc code=end

