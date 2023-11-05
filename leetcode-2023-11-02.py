"""
Question Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def get_all_nodes(self, root, l):
        if root.val is not None:
            l.append(root.val)
            if root.left:
                self.get_all_nodes(root.left,l)
            if root.right:
                self.get_all_nodes(root.right,l)

    def has_average(self,root):
        l = []
        self.get_all_nodes(root,l)
        return root.val==(sum(l)//len(l))


    def get_data(self,root, d):
        if root.val is not None:
            d.append((root.val,self.has_average(root)))
            if root.left:
                self.get_data(root.left, d)
            if root.right:
                self.get_data(root.right, d)

    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        d = []
        self.get_data(root, d)
        return len([k for k,v in d if v is True])
        