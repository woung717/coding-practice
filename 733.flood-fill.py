#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from queue import Queue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        queue = Queue()

        def check_boundary(r: int, c: int):
            return 0 <= r < len(image) and 0 <= c < len(image[0])

        start_color = image[sr][sc]
        queue.put((sr, sc))
        
        while not queue.empty():
            r, c =  queue.get()

            for o_r, o_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_r, next_c = r + o_r, c + o_c

                if check_boundary(next_r, next_c) and \
                    (next_r, next_c) not in visited and \
                    image[next_r][next_c] == start_color:
                    queue.put((next_r, next_c))
                
            image[r][c] = color
            visited.add((r, c))

        return image

        
        
# @lc code=end

