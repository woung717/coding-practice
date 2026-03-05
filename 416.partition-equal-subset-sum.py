#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from collections import defaultdict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = defaultdict(bool)

        if total % 2 == 1:
            return False
        
        def recurse(i: int, remain: int):
            if (i, remain) in dp:
                return dp[(i, remain)]
            
            if remain == 0:
                return True
            
            if remain < 0 or i == len(nums):
                return False
            
            ret = recurse(i + 1, remain - nums[i]) or recurse(i + 1, remain)
            dp[(i, remain)] = ret

            return ret
            
        return recurse(0, total // 2)
        
# @lc code=end

