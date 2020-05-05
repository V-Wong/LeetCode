"""
https://leetcode.com/problems/longest-palindromic-substring/submissions/

Given a string s, find the longest palindromic substring in s.

Note: same looping structure as solution for "Palindromic Substring".
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        memo[i][j] determines if s[i..j] is a palindrome.
        Consider all substrings 2 <= length <= len(s).
        Find the one that is the longest palindrome.
        """
        
        longest_length = 0
        longest_string = s[0] if s else ""
        
        memo = [[False for _ in s] for _ in s]
        for i in range(len(s)):
            memo[i][i] = True
        
        for length in range(2, len(s) + 1):
            for start in range(len(s) - length + 1):
                end = start + length - 1
                if (length == 2 and s[start] == s[end]
                        or s[start] == s[end] and memo[start + 1][end - 1]):
                    if length > longest_length:
                        longest_string = s[start:end + 1]
                        longest_length = length
                    memo[start][end] = True
                    
        return longest_string