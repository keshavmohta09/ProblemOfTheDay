"""
Question Link: https://leetcode.com/problems/house-robber/description/?envType=daily-question&envId=2024-01-21
"""

from typing import List


class Solution:
    def get_answer(self, nums, dp, ind=0):
        if len(nums) <= ind:
            return 0
        if dp[ind] == -1:
            dp[ind] = max(
                (nums[ind] + self.get_answer(nums, dp, ind + 2)),
                self.get_answer(nums, dp, ind + 1),
            )
        return dp[ind]

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [-1] * len(nums)
        return self.get_answer(nums, dp=dp)
