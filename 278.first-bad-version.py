#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (44.23%)
# Likes:    8261
# Dislikes: 3269
# Total Accepted:    1.6M
# Total Submissions: 3.7M
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
# 
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
# 
# You are given an API bool isBadVersion(version) which returns whether version
# is bad. Implement a function to find the first bad version. You should
# minimize the number of calls to the API.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# 
# 
# Example 2:
# 
# 
# Input: n = 1, bad = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= bad <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         left, right = 1, n 

#         while left <= right:
#             middle = int((right + left) / 2)

#             if isBadVersion(middle):
#                 right = middle - 1
#             else:
#                 left = middle + 1


#         return left

from bisect import bisect_left

class Solution:
    def firstBadVersion(self, n: int) -> int:

        class Versions: 
            def __getitem__(_, i): return i
            
        return bisect_left(
            Versions(), 
            x=True, 
            lo=1, 
            hi=n, 
            key=lambda x: isBadVersion(x)
        )

# @lc code=end

