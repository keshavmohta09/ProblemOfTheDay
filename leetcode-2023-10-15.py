"""
Question Link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/?envType=daily-question&envId=2023-11-15
"""
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        arr[0] = 1

        for i in range(1,len(arr)):
            if abs(arr[i-1]-arr[i])>1:
                arr[i] = arr[i-1]+1

        return arr[-1]