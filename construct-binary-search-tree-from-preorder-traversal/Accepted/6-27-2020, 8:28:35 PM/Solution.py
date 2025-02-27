// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            if stack[-1].val > i:
                stack[-1].left = TreeNode(i)
                stack.append(stack[-1].left)
            else:
                temp = None
                while stack and stack[-1].val < i :
                    temp = stack.pop()
                temp.right = TreeNode(i)
                stack.append(temp.right)
        return root