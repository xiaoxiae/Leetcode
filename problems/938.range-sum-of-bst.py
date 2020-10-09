# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive_sum(self, current, L, R):
        total = current.val if L <= current.val <= R else 0

        if current.left is not None:
            total += self.recursive_sum(current.left, L, R)
        if current.right is not None:
            total += self.recursive_sum(current.right, L, R)

        return total

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.recursive_sum(root, L, R)
