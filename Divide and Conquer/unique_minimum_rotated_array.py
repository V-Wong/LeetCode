"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Find the minimum in an array that is sorted by rotated by a pivot.
Assume there are no duplicate elements in the array.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Modified binary search:
            - If middle element is greater than last element:
                - Then left half is sorted and pivot is on the right.
                - Continue searching on the right.
            - Otherwise:
                - Right half is sorted and pivot is on the left (possibly the mid)
                - Continue searching on the left

        Continue doing this until we've hit a sorted sequence or we've reduced to a single element. 
        """

        start, end = 0, len(nums) - 1
        
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]

            mid = (start + end) // 2
            
            if nums[mid] >= nums[end]:
                start = mid + 1
            else:
                end = mid
                
        return nums[start]