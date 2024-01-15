"""
Question Link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/?envType=daily-question&envId=2024-01-15
"""
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        first = []
        second = []

        lost_ever = {}
        for w, l in matches:
            lost_ever[l] = lost_ever.get(l, 0) + 1

        for w, l in matches:
            if not lost_ever.get(w) and w not in first:
                first.append(w)

            if lost_ever[l] == 1:
                second.append(l)
        return [sorted(first), sorted(second)]
