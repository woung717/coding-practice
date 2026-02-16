#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Hard (38.91%)
# Likes:    11780
# Dislikes: 1865
# Total Accepted:    1M
# Total Submissions: 2.7M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
# 
# 
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
# 
# 
# Given two words, beginWord and endWord, and a dictionary wordList, return the
# number of words in the shortest transformation sequence from beginWord to
# endWord, or 0 if no such sequence exists.
# 
# 
# Example 1:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot"
# -> "dog" -> cog", which is 5 words long.
# 
# 
# Example 2:
# 
# 
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
# 
# 
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def transformable_dict(word_list):
            ret = defaultdict(list)

            for word in word_list:
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    ret[pattern].append(word)
            
            return ret
        
        queue = deque([(beginWord, 1)])
        seen = set()

        if endWord not in wordList:
            return 0

        transformables = transformable_dict(set(wordList + [endWord]))
        
        while len(queue) > 0:
            current_word, depth = queue.popleft()

            if depth <= len(wordList) + 1 and current_word == endWord:
                return depth

            seen.add(current_word)

            for i in range(len(current_word)):
                w = current_word[:i] + '*' + current_word[i + 1:]
                for next_word in transformables[w]:
                    if next_word not in seen:
                        queue.append((next_word, depth + 1))
        
        return 0


# @lc code=end

