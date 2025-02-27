// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum = 0
        if not root:
            return 0
        if root.val % 2 == 0:
            if root.left and root.left.left:
                sum += root.left.left.val
            if root.left and root.left.right:
                sum += root.left.right.val
            if root.right and root.right.left:
                sum += root.right.left.val
            if root.right and root.right.right:
                sum += root.right.right.val
        sum += self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
        return sum
        
'''

sum = 0
if node.val % 2 == 0:
    sum += node.

'''