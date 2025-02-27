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
        arr=[]
        queue=[root]
        while queue:
            node = queue.pop(0)
            arr.append(node.val)
            if node.left:
                queue = [node.left]+queue
            if node.right:
                queue = [node.right]+queue
        return arr
                