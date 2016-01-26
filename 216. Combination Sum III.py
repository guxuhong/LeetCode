"""
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Ensure that numbers within the set are sorted in ascending order.

Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combination(self, ans, temp, k, start, n):
            if k > 1:
                for i in range(start, 9):
                    if n >= 2*i + 1:
                        self.combination(ans, temp+[i], k-1, i+1, n-i)
                    else:
                        break
            elif k == 1 and start <= n <= 9:
                ans.append(temp + [n])
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.combination(ans, [], k, 1, n)
        return ans
