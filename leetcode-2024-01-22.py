"""
Question Link: https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)

        twice_num = -1
        missing_num = -1

        for i in nums:
            if arr[i - 1] == 0:
                arr[i - 1] = 1
            else:
                twice_num = i

        for i in range(len(arr)):
            if arr[i] == 0:
                missing_num = i + 1
                break
        return [twice_num, missing_num]
