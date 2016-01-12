"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:
•You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
•After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""

#版本一（我也不懂什么意思）
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length:
            sells = [None] * length
            buys = [None] * length
            sells[0], buys[0] = 0, -prices[0]
            for i in range(1, length):
                delta = prices[i] - prices[i-1]
                sells[i] = max(sells[i-1] + delta, buys[i-1] + prices[i])
                buys[i] = max(buys[i-1] - delta, sells[i-2] - prices[i] if i > 1 else None)
            return max(sells)
        return 0

#版本二
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        sells = [None] * length
        buys = [None] * length
        sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        buys[0], buys[1] = -prices[0], max(-prices[0], -prices[1])
        for i in range(2, length):
            sells[i] = max(sells[i-1], buys[i-1] + prices[i])
            buys[i] = max(buys[i-1], sells[i-2] - prices[i])
        return sells[-1]
