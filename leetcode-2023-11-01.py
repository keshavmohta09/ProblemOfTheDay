"""
Question Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_counts(self, root, d):
        i = root.val
        if i is not None:
            d[i] = d.get(i,0)+1
            if root.left:
                self.get_counts(root.left,d=d)
            if root.right:
                self.get_counts(root.right,d=d)

    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        self.get_counts(root,d)

        val = 0

        for k, v in d.items():
            if val<v:
                val = v

        return [k for k,v in d.items() if v==val]

        