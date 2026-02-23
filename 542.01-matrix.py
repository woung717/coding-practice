#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         ret = [[10**4 for _ in range(len(mat[0]))] for _ in range(len(mat))]

#         def search_zero(i: int, j: int, depth: int, visited: set) -> int:
#             visited.add((i, j))
            
#             ret = 10**4
#             for n, m in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#                 if 0 <= i + n < len(mat) and \
#                     0 <= j + m < len(mat[0]) and \
#                     (i + n, j + m) not in visited:
#                     ret = min(ret, search_zero(i + n, j + m, depth + 1, visited))

#             visited.remove((i, j))

#             return ret


#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 ret[i][j] = search_zero(i, j, 0, set()) if ret[i][j] else 0

#         return ret

# from collections import deque

# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         ret = [[10**4 for _ in range(len(mat[0]))] for _ in range(len(mat))]
#         visited = set()
#         queue = deque()

#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 if mat[i][j] == 0:
#                     queue.append((i, j, 0))
#                     ret[i][j] = 0

#         while len(queue) > 0:
#             x, y, step = queue.popleft()

#             visited.add((x, y)) 

#             if mat[x][y] == 1:
#                 ret[x][y] = min(ret[x][y], step)

#             for n, m in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#                 if 0 <= x + n < len(mat) and \
#                     0 <= y + m < len(mat[0]) and \
#                     (x + n, y + m) not in visited and \
#                     mat[x + n][y + m] == 1:
#                     queue.append((x + n, y + m, step + 1))

#         return ret

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ret = [[10**4 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    ret[i][j] = 0

        while len(queue) > 0:
            x, y = queue.popleft()

            for n, m in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= x + n < len(mat) and \
                    0 <= y + m < len(mat[0]) and \
                    ret[x + n][y + m] > ret[x][y] + 1:
                    ret[x + n][y + m] = ret[x][y] + 1
                    queue.append((x + n, y + m))

        return ret

# @lc code=end

