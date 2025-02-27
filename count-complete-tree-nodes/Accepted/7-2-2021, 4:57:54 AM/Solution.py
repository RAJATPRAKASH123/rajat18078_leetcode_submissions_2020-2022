// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(root):
            if not root:
                return 0
            return 1 + height(root.left)

        def nodeCount(root):
            if not root:
                return 0
            res = 0
            left_height =  height(root.left) 
            right_height = height(root.right)
            if left_height == right_height:
                res = 2 ** (left_height) + nodeCount(root.right)
            else:
                res = 2 ** (right_height) + nodeCount(root.left)
            return res
        return nodeCount(root)