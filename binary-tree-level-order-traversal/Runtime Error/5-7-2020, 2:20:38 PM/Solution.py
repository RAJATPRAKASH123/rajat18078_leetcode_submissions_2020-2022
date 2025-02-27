// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        arr=[[root.val]]
        queue=[root]
        if not root:
            return []
        while queue:
            temp_queue=[]
            temp_queue_val=[]
            while queue:
                node = queue.pop(0)
                if node.left:
                    temp_queue.append(node.left)
                    temp_queue_val.append(node.left.val)
                if node.right:
                    temp_queue.append(node.right)
                    temp_queue_val.append(node.right.val)
            queue = temp_queue
            if temp_queue_val:
                arr.append(temp_queue_val)
            temp_queue,temp_queue_val=[],[]
        return arr