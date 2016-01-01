"""
 Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
 Find the two elements that appear only once.
For example:
Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
Note:
    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

#我的渣渣代码：
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)
        return list(ans)
        
#大神的代码
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, (x for x in nums if x & xor & -xor))
        return [ans, ans ^ xor]
