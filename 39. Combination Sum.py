"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. 
The same repeated number may be chosen from C unlimited number of times. 
Note:
•All numbers (including target) will be positive integers.
•Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
•The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
 A solution set is: 
[7] 
[2, 2, 3] 
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = [[] for i in range(target + 1)]
        candidates.sort()
        for t in candidates:
            if t <= target:
                ans[t].append([t])
            for i in range(t, target + 1):
                for j in ans[i-t]:
                    ans[i].append(j + [t])
        return ans[target]
