"""
Question Link: https://leetcode.com/problems/construct-string-from-binary-tree/description/?envType=daily-question&envId=2023-12-08
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def make(self, root: Optional[TreeNode], s: str):
        s += str(root.val)
        if root.left:
            s += "("
            s = self.make(root=root.left, s=s)
            s += ")"

        if root.right:
            if not root.left:
                s += "()"
            s += "("
            s = self.make(root.right, s=s)
            s += ")"

        return s

    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = self.make(root, s="")
        return s
