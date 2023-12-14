"""
Question Link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/?envType=daily-question&envId=2023-12-14
"""
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # ----Approach 1 (TLE)------------
        # row_ind_sum = {}
        # r_grid = [[] for i in grid]

        # for col_ind in range(len(grid[0])):
        #     for row_ind in range(len(grid)):
        #         row = grid[row_ind]

        #         diff = row_ind_sum.get(row_ind,0)
        #         if not diff:
        #             for i in row:
        #                 if i==1:
        #                     diff+=1
        #                 else:
        #                     diff-=1
        #             row_ind_sum[row_ind] = diff
        #         temp = diff

        #         for i in range(len(grid)):
        #             if grid[i][col_ind]==1:
        #                 temp+=1
        #             else:
        #                 temp-=1
        #         r_grid[row_ind].append(temp)

        # return r_grid

        # -----Approach 2--------------
        # row_sum = []
        # col_sum = []

        # for row in grid:
        #     diff = 0
        #     for r in row:
        #         if r == 1:
        #             diff += 1
        #         else:
        #             diff -= 1
        #     row_sum.append(diff)

        # for col_ind in range(len(grid[0])):
        #     diff = 0
        #     for row in grid:
        #         if row[col_ind] == 1:
        #             diff += 1
        #         else:
        #             diff -= 1
        #     col_sum.append(diff)

        # for col_ind in range(len(grid[0])):
        #     for row_ind in range(len(grid)):
        #         grid[row_ind][col_ind] = row_sum[row_ind] + col_sum[col_ind]

        # return grid

        # ---------Approach 3---------------
        m = len(grid)
        n = len(grid[0])
        row_sum = [0] * m
        col_sum = [0] * n

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                row_sum[i] += grid[i][j]
                col_sum[j] += grid[i][j]

        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row_sum[i] + col_sum[j]) - (m + n)

        return grid
