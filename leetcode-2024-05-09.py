"""
Question Link: https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09
"""

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        result = 0
        for i in range(k):
            max_happiness = happiness.pop()
            value = max_happiness - i
            if value < 0:
                return result
            result += value

        return result
