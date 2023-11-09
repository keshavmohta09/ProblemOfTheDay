"""
Question Link: https://leetcode.com/problems/count-number-of-homogenous-substrings/?envType=daily-question&envId=2023-11-09
"""

class Solution:
    
    def fact_add(self,n):
        if n==0:
            return 0
        return n+self.fact_add(n-1)

    def countHomogenous(self, s: str) -> int:
        count = 0
        prev = ""
        r = 0
        for i in s:
            if not prev:
                prev = i
                count+=1
            elif prev==i:
                count+=1
            else:
                r+=self.fact_add(count)
                prev = i
                count = 1
        r+=self.fact_add(count)
        return r%((10**9)+7)
            
