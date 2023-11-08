"""
Question Link: https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/submissions/?envType=daily-question&envId=2023-11-08
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy:
            return t!=1

        dx = abs(sx-fx)
        dy = abs(sy-fy)
        
        return max(dx,dy)<=t
