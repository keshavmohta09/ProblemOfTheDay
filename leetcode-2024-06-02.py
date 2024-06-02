"""
Question Link: https://leetcode.com/problems/reverse-string/description/?envType=daily-question&envId=2024-06-02
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1

        while i<j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        
