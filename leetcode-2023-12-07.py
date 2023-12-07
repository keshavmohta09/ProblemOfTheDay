"""
Question Link: https://leetcode.com/problems/largest-odd-number-in-string/?envType=daily-question&envId=2023-12-07
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[: i + 1]

        return ""
