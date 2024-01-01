"""
Question Link: https://leetcode.com/problems/assign-cookies/description/?envType=daily-question&envId=2024-01-01
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gi = 0
        si = 0
        count = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                count += 1
                gi += 1
                si += 1
            else:
                si += 1

        return count
