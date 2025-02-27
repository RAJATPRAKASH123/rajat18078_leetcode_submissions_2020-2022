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
            res[col][row].append(root.val)
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
        dfs(root)
        cols_arr = sorted( list(res.keys()) ) # keys of res
        vert_traversal = []
        for column in cols_arr:
            rows = res[column]
            row_arr = sorted(list(rows.keys()))
            cur_col = []
            # print(column, row_arr)
            for row in row_arr:
                cur_col.extend(sorted(res[column][row]) )
            vert_traversal.append(cur_col)
        return vert_traversal