"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        if length == 0:
            return 0
        ans = [triangle[0][0]]
        for i in range(1, length):
            ans.append(triangle[i][-1] + ans[-1])
            for j in range(i - 1, 0, -1):
                ans[j] = min(ans[j], ans[j-1]) + triangle[i][j]
            ans[0] += triangle[i][0]
        return min(ans)
