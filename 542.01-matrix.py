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
        m, n = len(mat), len(mat[0])
        ret = [[10**4 for _ in range(n)] for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ret[i][j] = 0
                    queue.append((i, j))

        while len(queue) > 0:
            r, c = queue.popleft()

            for o_r, o_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_r, new_c = r + o_r, c + o_c
                if 0 <= new_r < m and \
                    0 <= new_c < n and \
                    ret[new_r][new_c] > ret[r][c] + 1 and \
                    mat[new_r][new_c] == 1:
                    ret[new_r][new_c] = ret[r][c] + 1
                    queue.append((new_r, new_c))

        return ret
    
# @lc code=end

