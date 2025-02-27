// https://leetcode.com/problems/minimum-distance-between-bst-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return -1
        temp = []
        def inorder(root):
            nonlocal temp
            if root:
                inorder(root.left)
                temp.append(root.val)
                inorder(root.right)
        ans = float("inf")
        inorder(root)
        for i in range(1,len(temp)):
            if temp[i]-temp[i-1] < ans:
                ans = temp[i]-temp[i-1]
        return ans