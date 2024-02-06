"""
Question Link: https://leetcode.com/problems/group-anagrams/description/?envType=daily-question&envId=2024-02-06
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            d.setdefault("".join(sorted(i)), []).append(i)

        return list(d.values())
