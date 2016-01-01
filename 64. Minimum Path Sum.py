"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = [grid[0][i] for i in range(n)]
        for i in range(1, n):
            ans[i] += ans[i-1]
        for i in range(1, m):
            ans[0] += grid[i][0]
            for j in range(1, n):
                ans[j] = grid[i][j] + min(ans[j-1], ans[j])
        return ans[-1]
