"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
 Could you do this in-place?
"""

#我的渣渣代码：
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        times, length = len(matrix) / 2, len(matrix)
        for i in range(times):
            for j in range(i, length-i-1):
                matrix[i][j], matrix[j][length-i-1] = matrix[j][length-i-1], matrix[i][j]
                matrix[i][j], matrix[length-i-1][length-j-1] = matrix[length-i-1][length-j-1], matrix[i][j]
                matrix[i][j], matrix[length-j-1][i] = matrix[length-j-1][i], matrix[i][j]
            i += 1
            
#大神代码：
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for column in matrix:
            column.reverse()
