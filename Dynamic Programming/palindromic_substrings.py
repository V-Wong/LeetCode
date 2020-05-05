"""
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes 
are counted as different substrings even they consist of same characters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        O(n^2) matrix chain multiplication modification.

        memo[i][j] determines whether s[i..j] is palindromic.

        Consider all substrings of 2 <= length <= len(s).
        For each substring, consider all possible starting indexes.
        Compute the corresponding ending index.
        To check whether s[start..end] is a palindrome, we check:
            - if s[start] == s[end] and
            - memo[start + 1][end - 1] is True.
        """

        memo = [[False for _ in s] for _ in s]
        
        for i in range(len(s)):
            memo[i][i] = True
            
        numPalindromes = len(s)
        for length in range(2, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1
                if (length == 2 and s[start] == s[end]
                        or s[start] == s[end] and memo[start + 1][end - 1]):
                    numPalindromes += 1
                    memo[start][end] = True
                        
        return numPalindromes
