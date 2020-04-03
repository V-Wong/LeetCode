from typing import List

"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

A sorted array was rotated along some unknown pivot.
Find the target element within the array in O(log(n)) time.
"""


class Solution:
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


class AlternativeSolution:
    def search(self, nums: List[int], target: int) -> int:
        """
        We first perform a modified binary search to find the rotation value.
        This rotation amount then splits the array into two sorted subarrays.
        We then perform a standard binary search on either of these subarrays
        to find the desired element.
        """

        def find_rotation_value(nums: List[int], low: int, high: int):
            """
            Finding the rotation value is equivalent to finding the smallest element.
            """

            mid = (low + high) // 2
            # Our search has reduced to one element
            # This element must be the smallest element
            if low == mid == high:
                return mid
            # Smallest element lies in nums[mid + 1]..nums[high]
            elif nums[mid] > nums[high]:
                return find_rotation_value(nums, mid + 1, high)
            # Smallest element lies in nums[low]..nums[mid]
            # Note that this goes up to nums[mid] and not nums[mid - 1]
            # nums[mid] may be the smallest element, but this needs to be verified
            else:
                return find_rotation_value(nums, low, mid)
                    
        def binary_search(nums: List[int], low: int, high: int, target: int):
            if low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(nums, mid + 1, high, target)
                else:
                    return binary_search(nums, low, mid - 1, target)
            else:
                return -1

        if nums:
            rotation_value = find_rotation_value(nums, 0, len(nums) - 1)
            if nums[rotation_value] <= target <= nums[len(nums) - 1]:
                return binary_search(nums, rotation_value, len(nums) - 1, target)
            else:
                return binary_search(nums, 0, rotation_value, target)
        else:
            return -1