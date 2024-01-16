"""
Question Link: https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=daily-question&envId=2024-01-16
"""

from random import randint


class RandomizedSet:
    def __init__(self):
        self.l = {}

    def insert(self, val: int) -> bool:
        l = self.l
        if l.get(val):
            l[val] = l[val] + 1
            return False

        l[val] = 1
        return True

    def remove(self, val: int) -> bool:
        l = self.l
        if l.get(val):
            l.pop(val)

        else:
            return False
        return True

    def getRandom(self) -> int:
        keys = list(self.l.keys())
        return keys and keys[randint(0, len(keys) - 1)] or 0


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
