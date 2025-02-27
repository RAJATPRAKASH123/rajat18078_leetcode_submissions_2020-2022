// https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = defaultdict(int)
        def money(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            take_money = root.val
            if root.left:
                take_money += money(root.left.left) + money(root.left.right)
            if root.right:
                take_money += money(root.right.left) + money(root.right.right)
            dont_take = money(root.left) + money(root.right)
            memo[root] = max(take_money, dont_take)
            return memo[root]
        
        return money(root)
                
'''

if turn == -1:

node : take it and make turn = 0 for next

       not take it make turn = 1 for next
       
       
if turn == 0:
    dont't take it call on next
    
    
'''