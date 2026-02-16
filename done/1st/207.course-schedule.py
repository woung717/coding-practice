#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (46.59%)
# Likes:    15831
# Dislikes: 671
# Total Accepted:    1.5M
# Total Submissions: 3.2M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        curriculums = defaultdict(list)
        seen = defaultdict(lambda: None)

        for c, p in prerequisites:
            curriculums[c].append(p)
            curriculums[p]

        def is_acyclic(node):
            if seen[node] == -1: return False
            if seen[node] == 1: return True

            seen[node] = -1
            for next in curriculums[node]:
                if is_acyclic(next) == False:
                    return False
            seen[node] = 1

            return True
        
        for i in curriculums.keys():
            if is_acyclic(i) == False:
                return False
        
        return True
    
# @lc code=end

