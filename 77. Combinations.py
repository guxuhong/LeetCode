"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def subcombine(ans, combinations):
            length = len(combinations[0])
            if length == k:
                for combination in combinations:
                    ans.append(combination)
            else:
                for i in range(len(combinations)):
                    copycombinations = []
                    for j in range(combinations[i][-1] + 1, n - k + length + 2):
                        copycombinations.append(combinations[i] + [j])
                    subcombine(ans, copycombinations)
        combinations = [[i] for i in range(1, n - k + 2)]
        ans = []
        subcombine(ans, combinations)
        return ans
