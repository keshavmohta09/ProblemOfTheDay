"""
Question Link: https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=daily-question&envId=2023-12-31
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    ans = max(ans, right - left - 1)

        return ans
