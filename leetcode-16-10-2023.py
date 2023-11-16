"""
Question Link: https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2023-11-16
"""

from typing import List


class Solution:

    # ------------Approach 1----------------------

    # def bin_sum(self, num, ind=None):
    #     if ind is None:
    #         ind = len(num)-1
    #     if num[ind] == "0":
    #         num = num[:ind]+"1"+num[ind+1:]
    #         return num
    #     else:
    #         num = num[:ind]+"0"+num[ind+1:]
    #         return self.bin_sum(num=num, ind=ind-1)

    # def findDifferentBinaryString(self, nums: List[str]) -> str:
    #     num = nums[0].replace("1","0")
    #     if num not in nums:
    #         return num
    #     for i in range((2**len(nums))-1):
    #         num = self.bin_sum(num)
    #         if num not in nums:
    #             return num

    # --------------Approach 2-------------------

    def ones_complement(self,num):
        return "1" if num=="0" else "0"

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k = ""
        for i in range(len(nums)):
            k+=self.ones_complement(nums[i][i])
        return k