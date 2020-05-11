from typing import List

"""
https://leetcode.com/problems/island-perimeter/
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        View the grid as a graph where:
            - Each cell is a vertex.
            - There is an edge between each adjacent cell.
            
        Note: this method is very inefficient.
        """
        
        def dfSearch(grid: List[List[int]], i: int, j: int, seen: List[List[int]]):        
            if (0 <= i < len(grid) and 0 <= j < len(grid[0]) and not seen[i][j] and grid[i][j]):
                seen[i][j] = True
                count = 0
                count += dfSearch(grid, i + 1, j, seen)
                count += dfSearch(grid, i - 1, j, seen)
                count += dfSearch(grid, i, j + 1, seen)
                count += dfSearch(grid, i, j - 1, seen)
                
                if not 0 <= i + 1 < len(grid) or not grid[i + 1][j]:
                    count += 1
                if not 0 <= i - 1 < len(grid) or not grid[i - 1][j]:
                    count += 1
                if not 0 <= j + 1 < len(grid[0]) or not grid[i][j + 1]:
                    count += 1
                if not 0 <= j - 1 < len(grid[0]) or not grid[i][j - 1]:
                    count += 1
    
                return count
            else:
                return 0
            
        seen = [[False for _ in grid[0]] for _ in grid]
        
        # Try find the first cell of a connected component.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfSearch(grid, i, j, seen)
