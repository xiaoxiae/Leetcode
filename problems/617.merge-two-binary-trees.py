# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, c1, c2):
        c1.val += c2.val

        if c1.left is not None and c2.left is not None:
            self.recursive(c1.left, c2.left)
        if c1.left is None and c2.left is not None:
            c1.left = c2.left

        if c1.right is not None and c2.right is not None:
            self.recursive(c1.right, c2.right)
        if c1.right is None and c2.right is not None:
            c1.right = c2.right

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        self.recursive(t1, t2)
        return t1
