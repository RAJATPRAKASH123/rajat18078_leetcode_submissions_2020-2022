// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        ans = -1
        def inorder(root,k):
            nonlocal count
            nonlocal ans
            if root:
                inorder(root.left,k)
                count += 1
                if count == k:
                    ans = root.val
                inorder(root.right,k)        
        inorder(root,k)
        return ans