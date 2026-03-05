#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from bisect import bisect_right
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        value_list = self.time_map[key]

        if len(value_list) == 0:
            return ""
        
        found_index = bisect_right(value_list, timestamp, key=lambda x: x[0])

        if found_index == 0 and value_list[0][0] != timestamp:
            return ""

        return value_list[found_index - 1][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

