"""
Question Link: https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=daily-question&envId=2024-01-14
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1 = {}
        d2 = {}
        for i in word1:
            d1[i] = d1.get(i, 0) + 1
        for i in word2:
            d2[i] = d2.get(i, 0) + 1

        if set(d1.keys()) != set(d2.keys()):
            return False

        for letter, count in d2.items():
            if d1[letter] == count:
                d1.pop(letter)
                continue
            for letter1, count1 in d1.items():
                if count1 == count:
                    d1 = dict(d1)
                    d1[letter1] = d1[letter]
                    d1.pop(letter)
                    break

        return not bool(d1)
