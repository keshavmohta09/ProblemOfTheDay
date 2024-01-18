"""
Question Link: https://leetcode.com/problems/climbing-stairs/description/?envType=daily-question&envId=2024-01-18
"""


class Solution:
    def get_answer(self, l, n, d):
        if l == n:
            return 1
        if l > n:
            return 0
        if d.get(l):
            return d[l]
        d[l] = sum((self.get_answer(l + 1, n, d), self.get_answer(l + 2, n, d)))
        return d[l]

    def climbStairs(self, n: int) -> int:
        return self.get_answer(0, n, {})
