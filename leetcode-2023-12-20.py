"""
Question Link: https://leetcode.com/problems/buy-two-chocolates/description/?envType=daily-question&envId=2023-12-20
"""

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min = float("inf")
        s_min = float("inf")

        for price in prices:
            if price < min:
                s_min = min
                min = price
            elif price < s_min:
                s_min = price

        output = money - min - s_min

        return output if output >= 0 else money
