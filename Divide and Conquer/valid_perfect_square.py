"""
https://leetcode.com/problems/valid-perfect-square/

Determine num is a perfect square
without using sqrt().
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num
        
        while low <= high:
            mid = (low + high) // 2
            
            res = mid ** 2
            if res < num:
                low = mid + 1
            elif res > num:
                high = mid - 1
            else:
                return True
                
        return False