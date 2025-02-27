// https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res_inorder = []
        while stack:
            # print(stack)
            while root.left:
                stack.append(root.left)
                root = root.left
            res_inorder.append(stack.pop().val)
            if root.right:
                stack.append(root.right)
                root = root.right
        return res_inorder