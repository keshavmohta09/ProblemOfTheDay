"""
Question Link: https://leetcode.com/problems/isomorphic-strings/description/?envType=daily-question&envId=2024-04-02
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_map.setdefault(s[i], set()).add(i)
            t_map.setdefault(t[i], set()).add(i)

        if sorted(s_map.values(), key=lambda x: sorted(x)) == sorted(
            t_map.values(), key=lambda x: sorted(x)
        ):
            return True

        return False
