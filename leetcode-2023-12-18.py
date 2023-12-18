"""
Question Link: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/?envType=daily-question&envId=2023-12-18
"""
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # -------Approach 1---------------
        # nums.sort()
        # return (nums[-1]*nums[-2])-(nums[0]*nums[1])

        # -------Approach 2-------------------
        l1 = float("inf")
        l2 = float("inf")

        g1 = 0
        g2 = 0

        for n in nums:
            if n > g1:
                g2 = g1
                g1 = n
            elif n > g2:
                g2 = n

            if n < l1:
                l2 = l1
                l1 = n
            elif n < l2:
                l2 = n

        return (g1 * g2) - (l1 * l2)
