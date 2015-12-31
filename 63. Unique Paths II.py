"""
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ans = [0 for i in range(n)]
        ans[0] = (obstacleGrid[0][0] + 1) % 2
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ans[j] = 0
                elif j != 0:
                    ans[j] += ans[j-1]
        return ans[-1]
