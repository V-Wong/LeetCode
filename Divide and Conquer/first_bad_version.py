"""
https://leetcode.com/problems/first-bad-version/

Suppose you have n versions [1, 2, ..., n] 
and you want to find out the first bad one, 
which causes all the following ones to be bad.
"""


def firstBadVersion(self, n):
    """
    Iterative binary search.
    If mid is a bad version:
        - Continue searching on left half (including the current mid).
    Else, continue searching on right half (not including the current mid).
    """

    left, right = 1, n
    
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    
    return left


def firstBadVersion2(self, n):
    """
    Recursive binary search.
    If mid is a bad version, two cases:
        - Left neighbour is not bad, which means mid is first bad version.
        - Left neighbour is bad, continue searching in left half of array.
    Else:
        - Continue searching on right half.
    """

    def helper(low, high):
        mid = (low + high) // 2
        if low <= high:
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    return helper(low, mid - 1)
            else:
                return helper(mid + 1, high)

    return helper(0, n)