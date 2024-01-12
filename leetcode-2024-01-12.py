"""
Question Link: https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        half_n = n // 2

        c1 = 0
        c2 = 0

        for i in range(n):
            if s[i] in "aeiouAEIOU":
                if i < half_n:
                    c1 += 1
                else:
                    c2 += 1

        return c1 == c2
