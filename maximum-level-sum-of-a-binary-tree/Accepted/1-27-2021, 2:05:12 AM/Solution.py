// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        queue = [root]
        lot = [root.val]
        while queue:
            
            arr = []
            while queue:
                temp = queue.pop(0)
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            if arr:
                queue = arr
                lot += [sum([node.val for node in arr]) ]
        print(lot)
        return lot.index(max(lot))+1
            