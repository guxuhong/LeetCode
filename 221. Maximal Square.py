"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        temp, maxsize = [], 0
        for i in range(m):
            temp.append([0 for j in range(n)])
            if matrix[i][0] == '1':
                temp[i][0] = 1
                maxsize = 1
        for j in range(n):
            if matrix[0][j] == '1':
                temp[0][j] = 1
                maxsize = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    temp[i][j] = 0
                else:
                    temp[i][j] = min(temp[i-1][j], temp[i][j-1], temp[i-1][j-1]) + 1
                    maxsize = max(maxsize, temp[i][j])
        return maxsize * maxsize
