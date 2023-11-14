"""
Question Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2023-11-14
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if not d.get(s[i]):
                d[s[i]] = (i,i,1)
            else:
                count = d[s[i]][2]+1
                if i<d[s[i]][0]:
                    d[s[i]] = (i,d[s[i]][1],count)
                elif i>d[s[i]][1]:
                    d[s[i]] = (d[s[i]][0],i,count)
                else:
                    d[s[i]] = (d[s[i]][0], d[s[i]][1], count)
        
        r = 0
        for k,v in d.items():
            if v[0]!=v[1]:
                r+=len(set(s[v[0]+1:v[1]]))
        return r

            