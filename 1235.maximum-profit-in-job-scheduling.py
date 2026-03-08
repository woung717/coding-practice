#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start

# from bisect import bisect_right

# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]

#         jobs.sort(key=lambda x: x[1])

#         dp = [] # (end_time, max_profit)

#         for job_start, job_end, job_profit in jobs:
#             closest_end = bisect_right(dp, job_start, key=lambda x: x[0]) - 1

#             max_prev = 0
#             if closest_end >= 0:
#                 max_prev = dp[closest_end][1]

#             curr_profit = max_prev + job_profit

#             if len(dp) == 0:
#                 dp.append([job_end, curr_profit])
#             elif dp[-1][0] == job_end:
#                 dp[-1][1] = max(dp[-1][1], curr_profit)
#             else:
#                 new_max = max(curr_profit, dp[-1][1])
#                 dp.append([job_end, new_max])

#         return dp[-1][1]
    

from bisect import bisect_left
from functools import lru_cache

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort()

        @lru_cache
        def recurse(i: int):
            if i == len(jobs):
                return 0
            
            _, end, profit = jobs[i]

            next_i = bisect_left(jobs, end, key=lambda x:x[0])
            take = profit + recurse(next_i)
            skip = recurse(i + 1)

            return max(skip, take)
        
        return recurse(0)

# @lc code=end

