from typing import List
import math

"""
https://leetcode.com/problems/min-cost-climbing-stairs/

cost[i] gives the cost of the ith step. 
You can climb 1 or 2 steps at a time.
Find the minimum cost to the top.

"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        minCost[i] gives the minimum cost to reach the ith step.
        It follows the recurrence:
            - minCost[i] = min(minCost[i - 1], minCost[i - 2]) + cost[i].

        That is, the minimum cost to the ith step is equal to cost[i]
        plus the minimum of either the step 1 step before it
        or the step 2 steps before it.
        """

        minCost = [math.inf for _ in cost]
        minCost[0], minCost[1] = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            minCost[i] = min(minCost[i - 1], minCost[i - 2]) + cost[i]
            
        return min(minCost[-1], minCost[-2])