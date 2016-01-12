"""
You are given coins of different denominations and a total amount of money amount. 
rite a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1. 
Example 1:
 coins = [1, 2, 5], amount = 11
 return 3 (11 = 5 + 5 + 1) 
Example 2:
 coins = [2], amount = 3
 return -1. 
Note:
 You may assume that you have an infinite number of each kind of coin. 
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        infinite = 10000
        times = [infinite for i in range(amount+1)]
        times[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                times[j] = min(times[j], times[j-coins[i]] + 1)
        return times[amount] if times[amount] != infinite else -1
