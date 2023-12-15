"""
Question Link: https://leetcode.com/problems/destination-city/description/?envType=daily-question&envId=2023-12-15
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()
        destinations = set()

        for source, destination in paths:
            sources.add(source)
            destinations.add(destination)

        final_destination = tuple(destinations - sources)[0]

        return final_destination
