"""
Question Link: https://leetcode.com/problems/leaf-similar-trees/description/?envType=daily-question&envId=2024-01-09
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_sequence(self, root, seq):
        if not root:
            return

        if not (root.left or root.right):
            seq.append(root.val)
            return

        self.get_sequence(root.left, seq)
        self.get_sequence(root.right, seq)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1 = []
        s2 = []
        self.get_sequence(root=root1, seq=s1)
        self.get_sequence(root=root2, seq=s2)

        return s1 == s2
