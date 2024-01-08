"""
Question Link: https://leetcode.com/problems/range-sum-of-bst/?envType=daily-question&envId=2024-01-08
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        def get_total(root, low, high):
            nonlocal total
            if not root:
                return
            if root.val < low:
                return get_total(root=root.right, low=low, high=high)
            elif root.val > high:
                return get_total(root=root.left, low=low, high=high)
            else:
                total += root.val
                get_total(root=root.left, low=low, high=high)
                get_total(root=root.right, low=low, high=high)

        get_total(root=root, low=low, high=high)
        return total
