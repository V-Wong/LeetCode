from typing import List

"""
https://leetcode.com/problems/maximum-subarray/

Find the contiguous subarray with largest sum.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        max_ending_here records the largest possible non-negative
        subarray sum ending at the current element.
        
        Once max_ending_here becomes less than 0, it is no longer worth
        continuing this subarray. Instead we start our new
        subarray at the next element.
        
        E.g. consider: [-2,1,-3,4,-1,2,1,-5,4].
        
        -2 is immediately worthless.
        1 is useful and we set max_ending_here to 1.
        Once we reach -3, max_ending_here + (-3) = -2 < 0. 
        It is no longer worth continuing this subarray.
        Any subsequent subarray of non-negative integers
        must necssarily be larger than this subarray.
        It is not worth continuing this subarray by trying to 
        find larger positive values to compensate, instead 
        we just drop this subarray and find new ones.
        
        We keep continuing this process and record down
        the largest max_ending_here value in max_so_far.
        """
        
        max_ending_here = 0
        max_so_far = 0
        for num in nums:
            max_ending_here = max(0, max_ending_here + num)
            max_so_far = max(max_ending_here, max_so_far)
            
        return max_so_far if max_so_far > 0 else max(nums)