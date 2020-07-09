"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

The width of one level is defined as the length between the end-nodes
where null nodes in between are counted.

Find the maximum level width of a binary tree.
"""

from typing import List


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        Perform BFS while tracking the horizontal position of each node within its level.
        The left child has position 2 * pos, and right child has position 2 * pos + 1.
        Use this horizontal position to calculate the width of each level at the end.
        """
        
        def widthOfLevel(traversal: List[int]) -> int:
            return traversal[-1][-1] - traversal[0][-1]

        traversal = [[]]
        
        q = [(root, 0, 0)]
        
        maxLevel = 0
        while q:
            curNode, curLevel, pos = q.pop(0)
            
            if curNode and curLevel > maxLevel:
                maxLevel += 1
                traversal.append([])
            
            if curNode:                    
                q.append((curNode.left, curLevel + 1, 2 * pos))
                q.append((curNode.right, curLevel + 1, 2 * pos + 1))
                
                traversal[-1].append((curNode.val, curLevel, pos))
    
        return max([widthOfLevel(level) for level in traversal], default=0) + 1