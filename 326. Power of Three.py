"""
Given an integer, write a function to determine if it is a power of three. 
Follow up:
 Could you do it without using any loop / recursion? 
"""

import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        return abs(math.log(n) / math.log(3.0) - round(math.log(n) / math.log(3.0))) < 1e-10
