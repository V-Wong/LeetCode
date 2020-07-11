"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        For each num, we have two choices:
            - Include it in our set.
            - Exclude it in our set.
        We use recursion to try every combination of choices.
        
        Note: can optimise by using an index variable instead of slicing
              and also by using a set or similar data structure
              with a less costly merge operation.
        """
        
        def helper(nums: List[int], curSet: List[int]):
            if not nums:
                return [curSet]
            else:
                includeCur = helper(nums[1::], curSet.copy() + [nums[0]])
                excludeCur = helper(nums[1::], curSet.copy())

            return includeCur + excludeCur

        return helper(nums, [])


class AlternativeSolutions:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        We can represent every subset as a bitstring from 
        0 to 2 ** len(nums) - 1 where 0 denotes absence of 
        the given element, and 1 denotes the presence
        of the given element.
        """
        
        powerset = []
        
        for i in range(2 ** len(nums)):
            curSet = []
            for j in range(len(nums)):
                if i & (1 << j):
                    curSet.append(nums[j])
            powerset.append(curSet)
            
        return powerset
