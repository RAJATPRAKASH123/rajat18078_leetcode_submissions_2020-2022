// https://leetcode.com/problems/cousins-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue=[root]
        while queue:
            temp_stack=[]
            x_idx = -1;y_idx = -1
            while queue:
                node = queue.pop(0)
                if not node:
                    continue
                temp_stack += [node.left,node.right]
            queue=temp_stack[:]
            for i in range(len(temp_stack)):
                if temp_stack[i]:
                    if temp_stack[i].val == x:
                        x_idx = i
                    if temp_stack[i].val == y:
                        y_idx = i
            if x_idx != -1 and y_idx != -1:
                f = min(x_idx,y_idx);s = max(x_idx,y_idx)
                if s - f >= 2:
                    return True
                if f%2 == 1 and s%2==0 and s-f == 1:
                    return True
        return False