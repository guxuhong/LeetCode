"""
Follow up for "Remove Duplicates":
 What if duplicates are allowed at most twice?
For example,Given sorted array nums = [1,1,1,2,2,3], 
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""

#我的渣渣代码：
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prex1 = prex2 = None
        length = 0
        for i in range(len(nums)):
            if nums[i] != prex2:
                length += 1
                prex2 = prex1
                prex1 = nums[i]
            else:
                nums[i] = nums[-1] + 1
        nums.sort()
        return length
        
#大神的代码：
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)
        prev, curr = 1, 2
        while curr < len(nums):
            if nums[curr] == nums[prev-1] and nums[curr] == nums[prev]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        return prev + 1
