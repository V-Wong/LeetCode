"""
https://leetcode.com/problems/sort-integers-by-the-power-value/

The power of a a number is the number of steps to reach 1
following the Collatz sequence.

Find the number with the kth smallest power in [lo..hi].
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        We note that certain numbers can use powers of smaller numbers in its sequence.
        For example: (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
        The power of 12 here is just 1 + power(6). We already calculated the power of 6.
        Instead of recalculating, we just retrieve the result from cache.
        """

        cache = {}

        for i in range(lo, hi + 1):
            n, curPower = i, 0
            while n > 1:
                if n in cache:
                    curPower += cache[n]
                    break
                
                if n % 2 == 0:
                    n /= 2
                else:
                    n = 3 * n + 1
                    
                curPower += 1
                
            cache[i] = curPower

        return sorted(cache.keys(), key=cache.get)[k - 1]