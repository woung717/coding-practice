#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from collections import Counter

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for count in Counter(nums).values():
#             if count > 1:
#                 return True
            
#         return False
    
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         neg_num_flag = 0
#         num_flag = 0

#         for n in nums:
#             if n >= 0:
#                 if num_flag & (1 << n):
#                     return True
                
#                 num_flag |= 1 << n
#             else:
#                 if neg_num_flag & (1 << -n):
#                     return True
                
#                 neg_num_flag |= 1 << -n
        
#         return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
# @lc code=end

