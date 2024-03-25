#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (41.48%)
# Likes:    15042
# Dislikes: 624
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        found = [False]

        def search(i, j, word_index):
            if (i, j) in seen: 
                return
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] != word[word_index]:
                return
            
            if board[i][j] == word[word_index] and word_index == len(word) - 1:
                found[0] = True
                return

            seen.add((i, j))

            for o in {(-1, 0), (0, 1), (1, 0), (0, -1)}:
                search(i + o[0], j + o[1], word_index + 1)
            
            seen.remove((i, j))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, 0)
                if found[0]:
                    break
        
        return found[0]
# @lc code=end

