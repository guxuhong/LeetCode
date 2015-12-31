"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations. 
For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1]. 
"""

#我的渣渣代码：
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        def subpermute(nums, ans, result):
            if len(nums) == 0:
                ans.append(result)
            else:
                prex = None
                for i in range(len(nums)):
                    if nums[i] != prex:
                        subpermute(nums[:i]+nums[i+1:], ans, result[:]+[nums[i]])
                        prex = nums[i]
        subpermute(nums, ans, [])
        return ans
  
#大神的代码：
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0: return []
        if length == 1: return [nums]
        nums.sort()
        prex, ans = None, []
        for i in range(length):
            if nums[i] != prex:
                prex = nums[i]
                for l in self.permuteUnique(nums[:i]+nums[i+1:]):
                    ans.append([nums[i]] + l)
        return ans
