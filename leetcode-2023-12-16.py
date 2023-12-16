"""
Question Link: https://leetcode.com/problems/valid-anagram/description/?envType=daily-question&envId=2023-12-16
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
