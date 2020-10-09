# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveCreate(self, nums, i, j) -> TreeNode:
        if i == j:
            return None

        avg = (i + j) // 2

        return TreeNode(
            nums[avg],
            self.recursiveCreate(nums, i, avg),
            self.recursiveCreate(nums, avg + 1, j),
        )

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.recursiveCreate(nums, 0, len(nums))
