#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        
        chs = set()
        for word in wordList:
            for c in word:
                chs.add(c)
        
        def get_next_words(word: str) -> List[str]:
            ret = []

            for i in range(len(word)):
                for c in chs:
                    new_word = word[:i] + c + word[i + 1:]

                    if new_word in wordList:
                        ret.append(new_word)

            return ret
        
        changes = deque([(beginWord, 1)])
        visited = set()

        while len(changes) > 0:
            curr_word, step = changes.popleft()

            if curr_word == endWord:
                return step
            
            for next_word in get_next_words(curr_word):
                if next_word not in visited:
                    visited.add(next_word)
                    changes.append((next_word, step + 1))

        return 0


# @lc code=end

