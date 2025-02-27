// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        count_pal = 0
        def helper(root, cur):
            nonlocal count_pal
            if not root.left and not root.right:
                cur += str(root.val)
                xors = 0
                for i in range(len(cur)):
                    xors ^= int(cur[i])
                if len(cur) % 2 == 0 and xors == 0:
                    count_pal += 1
                elif len(cur) % 2 == 1 and cur.count(str(xors))%2 == 1:
                    count_pal += 1
                return 
            if root.left:
                helper(root.left, cur + str(root.val))
            if root.right:
                helper(root.right, cur + str(root.val))
        
        helper(root, "")
        return count_pal
