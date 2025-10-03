# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower, upper):
            if root is None:
                return True
            val = root.val
            if val <= lower or val >= upper:
                return False
            if not helper(root.left, lower, val):
                return False
            if not helper(root.right, val, upper):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))
