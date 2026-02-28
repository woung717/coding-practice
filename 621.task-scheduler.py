#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from heapq import heappush_max, heappop_max, heapify_max
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ret = 0
        heap = [(n, t) for t, n in Counter(tasks).items()]
        heapify_max(heap)

        while len(heap) > 0:
            processing_tasks = []
            for _ in range(n + 1):
                if len(heap) == 0:
                    break
            
                remaining, task = heappop_max(heap)
                processing_tasks.append((remaining, task))

            n_processed = len(processing_tasks)
            
            for remaining, task in processing_tasks:
                if remaining - 1 > 0:
                    heappush_max(heap, (remaining - 1, task))
            
            if len(heap) > 0:
                ret += n + 1
            else:
                ret += n_processed

        return ret

# @lc code=end

