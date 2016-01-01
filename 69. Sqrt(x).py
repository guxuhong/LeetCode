"""
Implement int sqrt(int x).
Compute and return the square root of x.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        EPS, last, val = 0.00000001, 0.0, x
        while abs(last- val) > EPS:
            last = val
            val = (val + x*1.0 / val) / 2.0
        ans = int(val)
        if ans * ans > x:
            ans -= 1
        return ans
