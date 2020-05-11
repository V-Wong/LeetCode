from typing import List
from collections import defaultdict

"""
https://leetcode.com/problems/valid-square/

Determine if 4 points in Z^2 can form a square.
"""


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        Calculate all pairs of distances.
        Use a dict to store the distance: count.
        A square will have 2 unique distances:
            - Side length: which occurs 4 times.
            - Diagonal length: which occurs 2 times.
        """
        
        def calculateDistance(p1: List[int], p2: List[int]) -> int:
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        
        lengths = defaultdict(lambda: 0)
        
        points = [p1, p2, p3, p4]
        
        for i in range(len(points) - 1):
            for j in range(i, len(points)):
                if points[i] != points[j]:
                    lengths[calculateDistance(points[i], points[j])] += 1

        return list(lengths.values()) in ([4, 2], [2, 4])
