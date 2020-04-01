from typing import List

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

A sorted array was rotated along some unknown pivot.
Find the target element within the array in O(log(n)) time.
"""

def search(self, nums: List[int], target: int) -> int:
    """
    We approach this problem with a modified binary search.
    Whenever we bisect the array, at least one half must be sorted.
    Whichever half we find to be sorted, we check if our target lies in that half.
    If it does, we continue our search in the sorted half, else we continue 
    our search on the unsorted half.

    Consider the following example:
        [3, 4, 5, 1, 2].
    If we look between 5 and 1:
        - When we move left, all elements on the left are sorted.
        - When we move right, all elements on the right are sorted.
    """

    def helper(nums: List[int], low: int, high: int, target: int) -> int:
        if low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # Left half is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    return helper(nums, low, mid - 1, target)
                else:
                    return helper(nums, mid + 1, high, target)
            # Right half is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    return helper(nums, mid + 1, high, target)
                else:
                    return helper(nums, low, mid - 1, target)
        else:
            return -1

        return helper(nums, 0, len(nums) - 1, target)