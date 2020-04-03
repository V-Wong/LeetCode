from typing import Dict

"""
https://leetcode.com/problems/climbing-stairs/submissions/

Find all the unique ways to reach the top of a stair case
if you can climb in steps of 1 or 2 at a time.

Note: this is equivalent to generating Fibonacci numbers.
"""

def climbStairs(self, n: int, cache: Dict[int, int]={-1: 1, 0: 1, 1: 1}) -> int:
    """ 
    Recursive memoization approach.
    """
    
    if n in cache:
        return cache[n]
    else:
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        cache[n] = res
        return res


def climbStairs2(self, n: int) -> int:
    """
    Iterative approach.
    """

    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
        
    return b