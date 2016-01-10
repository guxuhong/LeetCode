"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 0:
            return 0
        ans, low = 0, prices[0]
        for i in range(1, length):
            if prices[i] < low:
                low = prices[i]
            else:
                ans = max(ans, prices[i] - low)
        return ans
