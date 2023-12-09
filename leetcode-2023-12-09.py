"""
Question Link: https://leetcode.com/problems/binary-tree-inorder-traversal/?envType=daily-question&envId=2023-12-09
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def make(self, root: Optional[TreeNode], l: List) -> None:
        if root.left:
            self.make(root=root.left, l=l)
        l.append(root.val)
        if root.right:
            self.make(root=root.right, l=l)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = []
        self.make(root=root, l=l)
        return l
