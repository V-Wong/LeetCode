from typing import List

"""
https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        View the image as an undirected graph where:
            - Each pixel is a vertex.
            - There is an edge between each adjacent pixel (not including diagonal).
        """
        
        def dfSearch(image: List[List[int]], i: int, j: int,
                     startColor: int, newColor: int, seen: List[List[int]]):        
            if (0 <= i < len(image) and 0 <= j < len(image[0])
                    and not seen[i][j] and image[i][j] == startColor):
                seen[i][j] = True
                dfSearch(image, i + 1, j, startColor, newColor, seen)
                dfSearch(image, i - 1, j, startColor, newColor, seen)
                dfSearch(image, i, j + 1, startColor, newColor, seen)
                dfSearch(image, i, j - 1, startColor, newColor, seen)
                image[i][j] = newColor

        seen = [[False for _ in image[0]] for _ in image]
        dfSearch(image, sr, sc, image[sr][sc], newColor, seen)
        return image