from typing import List


"""
https://leetcode.com/problems/house-robber/

Maximise the total you can rob if you can't rob adjacent houses.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        memo[i] stores the maximum total you can rob ending at house i.
        
        Set memo[i] = nums[i] for all i initially. Then utilise the recurrence:
            - memo[i] = max(memo[i - 2] + memo[i], memo[i - 3] + memo[i]).
            
        That is, the maximum we can rob ending at the ith house 
        is equal the amount at the ith house plus the maximum total ending at either:
            - The house 2 houses before or
            - The house 3 houses before.
            
        Note that we can optimise space by using two variables instead of a memo array.
        """
        
        if not nums:
            return 0
        elif len(nums) < 3:
            return max(nums)
        
        memo = [num for num in nums]
        memo[2] = memo[0] + memo[2]
   
        for i in range(3, len(nums)):
            memo[i] = memo[i] + max(memo[i - 2], memo[i - 3])

        return max(memo[-1], memo[-2])