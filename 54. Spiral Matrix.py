"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order. 
For example,
 Given the following matrix: 
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]. 
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while i < (m+1)/2 and j < (n+1)/2:
            if j == n-j-1:
                for k in range(i, m-i):
                    ans.append(matrix[k][j])
                break
            if i == m-i-1:
                for k in range(j, n-j):
                    ans.append(matrix[i][k])
                break
            for k in range(j, n-j-1):
                ans.append(matrix[i][k])
            for k in range(i, m-i-1):
                ans.append(matrix[k][n-j-1])
            for k in range(n-j-1, j, -1):
                ans.append(matrix[m-i-1][k])
            for k in range(m-i-1, i, -1):
                ans.append(matrix[k][j])
            i += 1
            j += 1
        return ans
