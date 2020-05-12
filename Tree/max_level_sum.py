from typing import List

"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Return the smallest level X such that the 
sum of all the values of nodes at level X is maximal.
"""


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfSearch(root: TreeNode, level: int, sums: List[int]=[]):
            if not root:
                return sums
            else:
                if level >= len(sums):
                    sums.append(0)
                sums[level] += root.val
                dfSearch(root.left, level + 1, sums)
                dfSearch(root.right, level + 1, sums)
                return sums

        sums = dfSearch(root, 0)
        return sums.index(max(sums)) + 1