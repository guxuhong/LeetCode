"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum. 
For example, given the array [−2,1,−3,4,−1,2,1,−5,4],the contiguous subarray [4,−1,2,1] has the largest sum = 6. 
"""

#我的渣渣代码
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, maxsum, cursum = 0, 0, 0
        maxsum = max(nums)
        if maxsum < 0: return maxsum
        for temp in nums:
            cursum += temp
            if cursum < 0 and abs(cursum) > ans:
                maxsum = max(maxsum, ans)
                ans = cursum = 0
            elif cursum > 0:
                ans += cursum
                cursum = 0
        return max(maxsum, ans)
        
#大神的代码：
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum, cursum = -100000, 0
        for temp in nums:
            if cursum < 0:
                cursum = 0
            cursum += temp
            maxsum = max(maxsum, cursum)
        return maxsum
