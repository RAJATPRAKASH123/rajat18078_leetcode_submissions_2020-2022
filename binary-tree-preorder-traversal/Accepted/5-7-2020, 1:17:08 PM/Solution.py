// https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # arr=[]
        # def helper(root):
        #     nonlocal arr
        #     if root:
        #         arr.append(root.val)
        #         helper(root.left)
        #         helper(root.right)
        # helper(root)
        # return arr
        if not root:
            return []
        arr=[]
        stack=[root]
        while stack:
            node = stack.pop()
            arr.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return arr
                