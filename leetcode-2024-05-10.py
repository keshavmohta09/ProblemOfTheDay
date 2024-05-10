"""
Question Link: https://leetcode.com/problems/k-th-smallest-prime-fraction/description/?envType=daily-question&envId=2024-05-10
"""

from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        new_arr = {}
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                new_arr[arr[i] / arr[j]] = [arr[i], arr[j]]

        return new_arr[sorted(list(new_arr.keys()))[k - 1]]
