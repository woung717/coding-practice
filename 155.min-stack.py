#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
from collections import deque


# class MinStack:

#     def __init__(self):
#         self.stack = deque()    

#     def push(self, val: int) -> None:
#         if len(self.stack) == 0 or val < self.stack[-1][1]:
#             self.stack.append((val, val))
#         else:
#             self.stack.append((val, self.stack[-1][1]))

#     def pop(self) -> None:
#         self.stack.pop()
        
#     def top(self) -> int:
#         return self.stack[-1][0] 

#     def getMin(self) -> int:
#         return self.stack[-1][1]


class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val) 

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

