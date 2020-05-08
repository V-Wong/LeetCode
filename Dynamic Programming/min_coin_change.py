from typing import List
import math

"""
https://leetcode.com/problems/coin-change/

coins: different denominations.
Find the minimum number of coins using 
the given denominations to sum up to amount.
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        memo[i]: minimal number of coins to sum up to amount = i.
        It follows the recurrence:
            - memo[i] = min{memo[i - coins[j]] + 1
                            s.t. 0 <= j <= len(coins)
                            and i - coins[j] >= 0}
    
        We can find the solution for i by considering all 
        previous solutions where adding a single coin attains i.
        This is given by memo[i - denominations[j]] + 1 where 
        j iterates over all coins.
        We find the minimum of this.
        """

        memo = [0] + [math.inf for _ in range(amount)]
        
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    memo[i] = min(memo[i], memo[i - coins[j]] + 1)
                
        return memo[-1] if memo[-1] != math.inf else -1