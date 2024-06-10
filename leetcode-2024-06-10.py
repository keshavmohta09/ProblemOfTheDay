"""
Question Link: https://leetcode.com/problems/height-checker/description/?envType=daily-question&envId=2024-06-10
"""

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = 0
        ind = 0
        for i in sorted(heights):
            if heights[ind]!=i:
                c+=1
            ind+=1
        return c
