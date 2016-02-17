"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, subset):
            ans.append(subset)
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[i - 1]:
                    dfs(i + 1, subset + [nums[i]])
        nums.sort()
        ans = []
        dfs(0, [])
        return ans
