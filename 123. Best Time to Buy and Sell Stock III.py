"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
 You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        preProfit = [0 for i in range(length)]
        postProfit = [0 for i in range(length)]
        
        low = prices[0]
        for i in range(1, length):
            low = min(low, prices[i])
            preProfit[i] = max(preProfit[i-1], prices[i] - low)
            
        high = prices[-1]
        for i in range(length-2, -1, -1):
            high = max(high, prices[i])
            postProfit[i] = max(postProfit[i-1], high - prices[i])
        
        maxprofit = 0
        for i in range(length):
            maxprofit = max(maxprofit, preProfit[i] + postProfit[i])
        return maxprofit
