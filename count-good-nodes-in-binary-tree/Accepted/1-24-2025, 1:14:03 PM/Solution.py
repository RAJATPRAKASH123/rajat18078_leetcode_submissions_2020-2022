// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodes(root, curMax=float("-inf")):
            count = 0
            if root.val >= curMax:
                count += 1
                curMax = root.val
            if root.left:
                count += goodNodes(root.left, curMax)
            if root.right:
                count += goodNodes(root.right, curMax)
            return count
        return goodNodes(root)