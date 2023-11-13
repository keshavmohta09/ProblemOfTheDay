"""
Question Link: https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2023-11-13
"""
class Solution:
    def sortVowels(self, s: str) -> str:
        l = [i for i in s if i in "AEIOUaeiou"]
        l.sort()

        m = ""
        ind = 0
        for i in s:
            if i in "AEIOUaeiou":
                m+=l[ind]
                ind+=1
            else:
                m+=i
        return m