"""
Question Link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
"""
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        r = []
        k = 0
        for i in pref:
            temp = k^i
            k = k^temp
            r.append(temp)
        return r