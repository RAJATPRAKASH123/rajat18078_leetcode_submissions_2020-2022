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
        stack=[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return arr
            node = stack.pop()
            arr.append(node.val)
            if node.right:
                root = node.right