# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricRecursive(self, p, q) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        return (
            p.val == q.val
            and self.isSymmetricRecursive(p.left, q.right)
            and self.isSymmetricRecursive(p.right, q.left)
        )

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isSymmetricRecursive(root.left, root.right)
