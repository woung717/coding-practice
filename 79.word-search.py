#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        
        def recurse(r: int, c: int, word_i: int, path: set):
            if board[r][c] != word[word_i]:
                return False
            
            if word_i >= len(word):
                return False
            
            if word_i == len(word) - 1 and board[r][c] == word[word_i]:
                return True

            path.add((r, c))

            ret = False
            for o_r, o_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                n_r, n_c = r + o_r, c + o_c

                if 0 <= n_r < len(board) and \
                    0 <= n_c < len(board[0]) and \
                    (n_r, n_c) not in path:

                    ret |= recurse(n_r, n_c, word_i + 1, path)

                    if ret:
                        break

            path.remove((r, c))

            return ret
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                ret = recurse(i, j, 0, path)

                if ret:
                    return ret

        return False

        
# @lc code=end

