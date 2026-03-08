#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []

        intervals.sort(key=lambda i: i[0])

        ret.append(intervals[0])
        
        for i in intervals[1:]:
            last_i = ret[-1]
            if i[0] <= last_i[1]:
                last_i[0] = min(last_i[0], i[0])
                last_i[1] = max(last_i[1], i[1])
            else:
                ret.append(i)

        return ret

                
        
# @lc code=end

