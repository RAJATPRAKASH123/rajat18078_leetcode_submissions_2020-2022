// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        height = defaultdict()
        height[None] = 0
        def height_fun(node):
            if not node:
                return 0
            if node in height:
                return height[node]
            height[node] = 1 + max(height_fun(node.left),height_fun(node.right) )
            return height[node]
        height_fun(root) # update the height dictionary
        
        memo = defaultdict(bool)
        def check(node):
            
            if not node:
                return True
            if node in memo:
                return memo[node]
            check_l_r = check(node.left) and check(node.right)
            h_l, h_r = 0, 0
            
            if node.left:
                h_l = height[node.left]
            if node.right:
                h_r = height[node.right]
            height_diff = abs( h_l - h_r ) <= 1 
            
            memo[node] = check_l_r and height_diff
        return check(root)