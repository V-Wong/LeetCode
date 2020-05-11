from typing import List
import math

"""
https://leetcode.com/problems/max-area-of-island/
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        View the grid as a graph where:
            - Each cell is a vertex.
            - There is an edge between each adjacent cell.
        """
        
        def dfSearch(grid: List[List[int]], i: int, j: int, seen: List[List[int]]) -> int:
            """
            Traverses a single component of the graph and returns the number 
            of islands in the component.
            """
            if (0 <= i < len(grid) and 0 <= j < len(grid[0])
                    and grid[i][j] and not seen[i][j]):
                seen[i][j] = True
                count = 0
                count += dfSearch(grid, i + 1, j, seen)
                count += dfSearch(grid, i - 1, j, seen)
                count += dfSearch(grid, i, j + 1, seen)
                count += dfSearch(grid, i, j - 1, seen)
                
                return 1 + count
            else:
                return 0
            
        seen = [[False for _ in grid[0]] for _ in grid]
        largestArea = -math.inf
        # Iterate over all cells to find all components
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not seen[i][j]:
                    largestArea = max(largestArea, dfSearch(grid, i, j, seen))
                    
        return largestArea