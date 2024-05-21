"""
Question Link: https://leetcode.com/problems/subsets/description/?envType=daily-question&envId=2024-05-21
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]

        for num in nums:
            temp = [num]
            for subset in list(all_subsets):
                all_subsets.append(subset + temp)

        return all_subsets
