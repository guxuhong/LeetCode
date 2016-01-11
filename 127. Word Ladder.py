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
        def oneDiffer(w1, w2):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
            if count == 1:
                return True
            return False
        levelvalues, level, used = [[beginWord]], 0, set()
        while True:
            levelvalues.append([])
            for t in levelvalues[level]:
                if t == endWord:
                    return level + 2
                used.add(t)
                for word in wordList:
                    if word not in used and oneDiffer(word, t):
                        levelvalues[level+1].append(word)
