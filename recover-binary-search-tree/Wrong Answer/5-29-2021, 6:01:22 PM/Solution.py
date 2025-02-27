// https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def update(root, a, b):
            if not root:
                return
            update(root.left, a, b)
            if root.val == a:
                root.val = b
            elif root.val == b:
                root.val = a
            update(root.right, a, b)
        
        first, sec, third = float('inf'), float('inf'), float('inf')
        swapped_node = set()
        if_one_found = -1
        def inorder(root):
            nonlocal first, sec, third, if_one_found
            if not root:
                return
            inorder(root.left)
            if third == float('inf'):
                pass
            elif sec == float('inf'):
                sec = third
            else:
                first = sec
                sec = third
            third = root.val
            if first != float('inf'):
                if first > sec:
                    swapped_node.add(first)
                    if_one_found = sec
            inorder(root.right)
        inorder(root) 
        
        # print(first, sec, third)
        if first == float('inf'): # only 2 nodes in tree
            update(root, sec, third)
            return
        if sec > third:
            swapped_node.add(third)
        
        swapped_node = list(swapped_node)
        print(swapped_node)
        if len(swapped_node) == 2:
            update(root, swapped_node[0], swapped_node[1])
            return
        update(root, swapped_node[0], if_one_found)
        