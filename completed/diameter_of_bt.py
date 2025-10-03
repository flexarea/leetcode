# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def tree_height(root):
            nonlocal diameter
            if root is None:
                return 0
            left = tree_height(root.left)
            right = tree_height(root.right)
            diameter = max(diameter, left + right)   # update diameter here
            return max(left, right) + 1

        tree_height(root)
        return diameter
