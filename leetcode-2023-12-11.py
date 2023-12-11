"""
Question Link: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/?envType=daily-question&envId=2023-12-11
"""
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        max_prev = arr[0]
        max_prev_freq = 0

        prev = arr[0]
        prev_freq = 0

        for i in arr:
            if i == prev:
                prev_freq += 1
            else:
                prev = i
                prev_freq = 1

            if prev_freq > max_prev_freq:
                max_prev = prev
                max_prev_freq = prev_freq

        return max_prev
