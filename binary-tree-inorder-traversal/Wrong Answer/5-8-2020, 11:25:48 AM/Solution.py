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
        arr=[]
        stack=[root]
        while stack:
            while root.left:
                stack.append(root.left)
                root = root.left
            root = stack.pop()
            arr.append(root.val)
            if root.right:
                stack.append(root.right)
                root = root.right
        return arr