"""
Question Link: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/solutions/4259221/beat-s-100-c-java-python-beginner-friendly/?envType=daily-question&envId=2023-11-07
"""

import math


class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """

        r = [int(math.ceil(dist[i]/speed[i])) for i in range(len(dist))]
        r.sort()

        count = 0
        for i in range(len(r)):
            r[i] -= i  
            if r[i] <= 0:  
                break
            count += 1 

        return count

