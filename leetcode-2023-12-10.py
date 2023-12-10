"""
Question Link: https://leetcode.com/problems/transpose-matrix/description/?envType=daily-question&envId=2023-12-10
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in matrix[0]:
            result.append([])

        for m in matrix:
            for i in range(len(m)):
                result[i].append(m[i])

        return result
