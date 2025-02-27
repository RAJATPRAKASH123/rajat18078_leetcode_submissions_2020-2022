// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def helper(root):
            if root:
                flatted_left = helper(root.left)
                flatted_right = helper(root.right)
                root.right = flatted_left
                if flatted_left:
                    temp = flatted_left
                    while temp.right:
                        temp = temp.right
                    temp.right = flatted_right
                    root.left = None
                else:
                    root.right = flatted_right
                return root
        helper(root)