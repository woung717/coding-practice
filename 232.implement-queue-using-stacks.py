#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        ret = None
        if len(self.stack2) > 0:
            ret = self.stack2.pop()

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return ret
        
    def peek(self) -> int:
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        ret = None
        if len(self.stack2) > 0:
            ret = self.stack2.pop()
            self.stack2.append(ret)

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return ret

    def empty(self) -> bool:
        return len(self.stack1) == 0


class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        self.stack1.append(x)

        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        ret = None
        if len(self.stack2) > 0:
            ret = self.stack2.pop()
        
        return ret
    
    def peek(self) -> int:
        ret = None

        if len(self.stack2) > 0:
            ret = self.stack2.pop()
            self.stack2.append(ret)

        return ret

    def empty(self) -> bool:
        return len(self.stack2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

