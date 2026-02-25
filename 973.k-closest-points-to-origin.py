#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

from heapq import heappop, heapify
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        def get_euc_dist_from_origin(x: int, y: int) -> float:
            return sqrt(x**2 + y**2)
        
        for p in points:
            x, y = p
            dist = get_euc_dist_from_origin(x, y)
            heap.append((dist, p))
        
        heapify(heap)

        return [heappop(heap)[1] for _ in range(k)]
        
# @lc code=end

