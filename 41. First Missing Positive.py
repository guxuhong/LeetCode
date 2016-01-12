"""
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.
"""

#python适用的方法
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        for n in nums:
            if n > 0:
                ans |= (1 << n)
        res = 0
        while ans > 0 and ans & 1:
            ans >>= 1
            res += 1
        return res

#通用的方法
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 1
        i = 0
        while i < length:
            if nums[i] > 0 and (nums[i] != i + 1) and (nums[i] - 1 < length) and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
            else:
                i += 1
        for i in range(length):
            if i + 1 != nums[i]:
                return i + 1
        return length + 1
