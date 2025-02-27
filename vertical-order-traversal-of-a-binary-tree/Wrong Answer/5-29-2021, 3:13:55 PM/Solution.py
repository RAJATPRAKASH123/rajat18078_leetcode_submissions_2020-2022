// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = defaultdict(lambda : defaultdict(list)) # column, row, its node.val
        def dfs(root, row=0, col=0):
            if not root:
                return
            res[col][row].append(root)
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
        dfs(root)
        
        cols_arr = list(res.keys()) # keys of res
        cols_arr.sort() #sorted
        vert_traversal = []
        for column in cols_arr:
            temp = []
            for row in res[column]:
                cur_row_nodes = res[column][row]
                cur_row_nodes = [node.val for node in cur_row_nodes]
                cur_row_nodes.sort()
                temp.extend(cur_row_nodes)
            vert_traversal.append(temp)
        return vert_traversal