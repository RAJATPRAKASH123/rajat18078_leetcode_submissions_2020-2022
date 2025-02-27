// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr1, arr2 = [],[]
        def helper(root, arr):
            if root:
                helper(root.left, arr)
                if not root.left and not root.right:
                    arr.append(root.val)
                helper(root.right, arr)
            return arr
        arr1 = helper(root1, arr1)
        arr2 = helper(root2, arr2)
        if arr1 == arr2:
            return True
        return False