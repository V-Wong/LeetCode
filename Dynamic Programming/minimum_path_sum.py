"""
https://leetcode.com/problems/minimum-path-sum/

Find the minimum path sum through a 2D grid
from top left to bottom right when you can
only move down or right.
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[math.inf for _ in range(n)]
                for _ in range(m)]

        memo[0][0] = grid[0][0]
        for j in range(1, n):
            memo[0][j] = grid[0][j] + memo[0][j - 1]
            
        for i in range(1, m):
            memo[i][0] = grid[i][0] + memo[i - 1][0]
            for j in range(1, n):  
                memo[i][j] = grid[i][j] + min(memo[i - 1][j], memo[i][j - 1])

        return memo[-1][-1]