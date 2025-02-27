// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, o: TreeNode, c: TreeNode, t: TreeNode) -> TreeNode:
        if not c:
            return None
        if c.val == t.val:
            return c
        temp1 = self.getTargetCopy(o, c.left, t)
        temp2 = self.getTargetCopy(o, c.right, t)
        if temp1:
            return temp1
        return temp2