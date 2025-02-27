// https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            if root:
                res.append(root.val)
                stack.pop()
                
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            if stack:
                root = stack[-1]
            else:
                return res[::-1]
            