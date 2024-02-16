"""
Question Link: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/?envType=daily-question&envId=2024-02-16
"""

from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = Counter(arr)
        t = list(d.values())
        t.sort()

        while k != 0:
            if t[0] > k:
                return len(t)
            elif t[0] == k:
                return len(t) - 1
            else:
                k -= t[0]
                t = t[1:]

        return len(t)
