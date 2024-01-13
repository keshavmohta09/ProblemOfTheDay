"""
Question Link: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-13
"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_d = {}
        for i in t:
            t_d[i] = t_d.get(i, 0) + 1

        s_d = {}
        for i in s:
            s_d[i] = s_d.get(i, 0) + 1

        c = 0
        for k, v in s_d.items():
            if k not in t_d:
                c += v
            else:
                temp = v - t_d[k]
                if temp > 0:
                    c += temp
        return c
