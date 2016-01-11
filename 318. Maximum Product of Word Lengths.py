"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. 
You may assume that each word will contain only lower case letters. If no such two words exist, return 0. 
Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
 Return 16
 The two words can be "abcw", "xtfn". 
Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
 Return 4
 The two words can be "ab", "cd". 
Example 3:
Given ["a", "aa", "aaa", "aaaa"]
 Return 0
 No such pair of words. 
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        length = len(words)
        ans = 0
        if length:
            words.sort(key = lambda x: len(x), reverse = True)
            nums = []
            for word in words:
                nums += [sum(1 << (ord(x) - ord('a')) for x in set(word))]
            for i in range(length):
                if pow(len(words[i]), 2) <= ans:
                    break
                for j in range(i+1, length):
                    if not (nums[i] & nums[j]):
                        ans = max(ans, len(words[i]) * len(words[j]))
                        break
        return ans
