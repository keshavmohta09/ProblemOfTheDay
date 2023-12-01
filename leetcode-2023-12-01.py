"""
Question Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/?envType=daily-question&envId=2023-12-01
"""
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
