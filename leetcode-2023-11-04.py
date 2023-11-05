"""
Question Link: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
"""
class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        return max((max(left) if left else 0), (n-min(right) if right else 0))