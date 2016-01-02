"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. 
Each number in C may only be used once in the combination. 
Note:
•All numbers (including target) will be positive integers.
•Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
•The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
 A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = [[] for i in range(target+1)]
        candidates.sort()
        for t in candidates:
            for i in range(target, t, -1):
                for j in ans[i - t]:
                    if j+[t] not in ans[i]:
                        ans[i].append(j + [t])
            if t <= target and [t] not in ans[t]:
                ans[t].append([t])
        return ans[target]
