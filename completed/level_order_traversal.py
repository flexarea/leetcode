# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_arr = []

        def recursive_traversal(level, root):
            if root is None:
                return

            if len(res_arr) <= level:
                res_arr.append([])

            res_arr[level].append(root.val)

            recursive_traversal(level+1, root.left)
            recursive_traversal(level+1, root.right)

        recursive_traversal(0, root)
        return res_arr
