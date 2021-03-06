"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
 Given n = 3, 
You should return the following matrix: [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[1 for i in range(n)] for j in range(n)]
        num, t = 1, 0
        while t <= (n-1)/2:
            if t == n-t-1:
                ans[t][t] = num
            for i in range(t, n-t-1):
                ans[t][i] = num
                ans[i][n-t-1] = num + n-2*t-1
                ans[n-t-1][n-i-1] = num + 2*(n-2*t-1)
                ans[n-i-1][t] = num + 3*(n-2*t-1)
                num += 1
            num += 3*(n-2*t-1)
            t += 1
        return ans
