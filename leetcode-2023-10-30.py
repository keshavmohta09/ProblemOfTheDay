"""
Question Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        s = []
        for a in arr:
            b = bin(a).split("b")[1]
            c_1 = b.count('1')
            s.append((a, (c_1,a)))

        s.sort(key=lambda x: x[1])

        return [i[0] for i in s]