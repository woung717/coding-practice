#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ret = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while len(queue) > 0:
            r, c, turn = queue.popleft()

            ret = max(ret, turn)

            for o_r, o_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                n_r, n_c = r + o_r, c + o_c

                if 0 <= n_r < len(grid) and \
                    0 <= n_c < len(grid[0]) and \
                    grid[n_r][n_c] == 1:
                    grid[n_r][n_c] = 2
                    queue.append((n_r, n_c, turn + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return ret

        
# @lc code=end

