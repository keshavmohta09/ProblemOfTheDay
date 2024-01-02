"""
Question Link: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/?envType=daily-question&envId=2024-01-02
"""

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        for num in nums:
            for ri in r:
                if num not in ri:
                    ri.append(num)
                    break
            else:
                r.append([num])
        return r
