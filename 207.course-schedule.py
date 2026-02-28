#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ret = True
        # matrix = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        # for prereq in prerequisites:
        #     take, pre_take = prereq
        #     matrix[take][pre_take] = True

        # def tracking(mat: List[List], take: int, visited: set):
        #     nonlocal ret

            
        #     if not ret:
        #         return
            
        #     if take in visited:
        #         ret = False
        #         return

        #     visited.add(take)

        #     for i, pre in enumerate(mat[take]):
        #         if pre:
        #             tracking(mat, i, visited)

        #     visited.remove(take)
        
        # for i in range(len(matrix)):
        #     tracking(matrix, i, set(), set())
        #     if not ret:
        #         break

        # return ret

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        finished = set()
        adj_list = [[] for _ in range(numCourses)]

        for take, prereq in prerequisites:
            adj_list[take].append(prereq)

        def track(prereq_list: List[List], take: int, visited: set):
            if take in finished:
                return True
            
            if take in visited:
                return False
            
            visited.add(take)

            for prereq in prereq_list[take]:
                if not track(prereq_list, prereq, visited):
                    return False

            finished.add(take)
            visited.remove(take)

            return True

        for i in range(numCourses):
            if not track(adj_list, i, set()):
                return False
        
        return True



# @lc code=end

