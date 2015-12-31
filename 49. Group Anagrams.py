"""
Given an array of strings, group anagrams together. 
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
 Return: 
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
1.For the return value, each inner list's elements must follow the lexicographic order.
2.All inputs will be in lower-case.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans, dictionary, index = [], {}, 0
        for s in strs:
            t = ''.join(sorted(list(s)))
            if t in dictionary:
                ans[dictionary[t]].append(s)
            else:
                dictionary[t] = index
                ans.append([s])
                index += 1
        for l in ans:
            l.sort()
        return ans
