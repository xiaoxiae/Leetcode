# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveLevel(self, root: TreeNode, depth: int):
        if root is None:
            return

        if len(self.levels) <= depth:
            self.levels.append([])
        self.levels[depth].append(root.val)

        self.recursiveLevel(root.left, depth + 1)
        self.recursiveLevel(root.right, depth + 1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.levels = []
        self.recursiveLevel(root, 0)
        return list(reversed(self.levels))
