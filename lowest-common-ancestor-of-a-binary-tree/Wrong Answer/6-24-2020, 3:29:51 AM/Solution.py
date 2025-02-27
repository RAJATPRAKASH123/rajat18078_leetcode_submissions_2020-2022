// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root, key, arr): 
            if not root:
                return False
            if root.val == key.val:
                return True
            arr.append(root)
            if search(root.left, key, arr) or search(root.right, key, arr):
                return True
            
        arr1 = []
        search(root, p, arr1)
        arr2 = []
        search(root, q, arr2)
        print(arr1)
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        for i in range(len(arr1)):
            if arr1[i].val != arr2[i].val:
                return arr1[i-1]
        return arr1[len(arr1)-1]