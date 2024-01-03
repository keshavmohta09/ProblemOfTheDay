"""
Question Link: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2024-01-03
"""
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0]

        if len(bank) == 1:
            return 0

        count = 0

        for curr in bank[1:]:
            prev_1 = prev.count("1")
            curr_1 = curr.count("1")

            if curr_1 == 0:
                continue

            if prev_1 == 0:
                prev = curr
                continue

            count += prev_1 * curr_1
            prev = curr

        return count
