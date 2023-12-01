"""
Question Link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2023-11-17
"""
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        r = 0
        nums.sort()
        
        l = len(nums)
        for i in range(l//2 or 1):
            temp = nums[i]+nums[l-i-1]
            if temp>r:
                r = temp
        return r
        