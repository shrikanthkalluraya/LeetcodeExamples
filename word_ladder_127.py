# Leetcode - 127. Word Ladder

from collections import deque, defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0

        wordList = set(wordList)
        queue = deque([(beginWord, 1)])  # (current_word, depth)


        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            # Try changing every letter
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        queue.append((next_word, length + 1))
                        wordList.remove(next_word)  # avoid revisiting

        return 0
