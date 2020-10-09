# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + (
            max(self.minDepth(root.left), self.minDepth(root.right))
            if root.left is None
            and root.right is not None
            or root.left is not None
            and root.right is None
            else min(self.minDepth(root.left), self.minDepth(root.right))
        )
