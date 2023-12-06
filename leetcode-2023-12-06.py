"""
Question Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/?envType=daily-question&envId=2023-12-06
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        # --------Solution 1---------------
        # div = n//7
        # rem = n%7

        # r = 0

        # for i in range(div):
        #     r+=(28+(7*i))

        # rem_days = (rem*(rem+1))//2
        # r+=(rem_days+(rem*div))

        # return r

        # -----------Solution 2--------------
        week_count = n // 7
        remaining_days = n % 7

        total = ((week_count * (week_count - 1)) // 2) * 7
        total += week_count * 28
        total += ((remaining_days * (remaining_days + 1)) // 2) + (
            week_count * remaining_days
        )

        return total
