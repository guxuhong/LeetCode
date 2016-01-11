"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that: 
1.Only one letter can be changed at a time
2.Each intermediate word must exist in the word list

For example, 
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 return its length 5. 
Note:
•Return 0 if there is no such transformation sequence.
•All words have the same length.
•All words contain only lowercase alphabetic characters.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        q = []
        q.append((beginWord, 1))
        while q:
            current = q.pop(0)
            currentword, currentstep = current[0], current[1]
            if currentword == endWord:
                return currentstep
            for i in range(len(beginWord)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    nextword = currentword[:i] + j + currentword[i+1:]
                    if nextword in wordList and nextword != currentword:
                        q.append((nextword, currentstep+1))
                        wordList.remove(nextword)
        return 0
