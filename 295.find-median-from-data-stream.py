#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
# from heapq import heappush_max, heappop_max, heappush, heappop

# class MedianFinder:

#     def __init__(self):
#         self.max_heap = []
#         self.min_heap = []
        
#     def addNum(self, num: int) -> None:
#         if len(self.max_heap) == 0:
#             heappush_max(self.max_heap, num)
#             return 
        
#         if len(self.min_heap) == 0 or num < self.min_heap[0]:
#             heappush_max(self.max_heap, num)
#         else:
#             heappush(self.min_heap, num)

#         if len(self.max_heap) - len(self.min_heap) > 1:
#             move = heappop_max(self.max_heap)
#             heappush(self.min_heap, move)
#         elif len(self.min_heap) - len(self.max_heap) > 0:
#             move = heappop(self.min_heap)
#             heappush_max(self.max_heap, move)

#     def findMedian(self) -> float:
#         if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
#             return self.max_heap[0]
#         else:
#             return (self.max_heap[0] + self.min_heap[0]) / 2

from heapq import heappush_max, heappop_max, heappush, heappop

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        heappush_max(self.max_heap, num)
        move = heappop_max(self.max_heap)
        heappush(self.min_heap, move)

        if len(self.max_heap) < len(self.min_heap):
            move = heappop(self.min_heap)
            heappush_max(self.max_heap, move)

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return self.max_heap[0]
        else:
            return (self.max_heap[0] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

